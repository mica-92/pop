"""
pop_build_csv.py
================
Combina todos los archivos 81_*.csv en un único 81_all.csv listo para importar.

VERSIÓN NORMALIZADA:
- 5 productos reales: sticker, saliente, backlight, bicicletero, sombrilla
- La ubicación (SAL, MDQ, CABA, etc.) es atributo del establecimiento
- Un solo CSV por producto real (no por ubicación)

Uso:
  python pop_build_csv.py              → procesa todos los 81_*.csv del directorio
  python pop_build_csv.py --preview    → muestra resumen sin escribir nada
  python pop_build_csv.py --dir <ruta> → usa otro directorio como base
"""

import os
import sys
import re
import csv
import glob
import argparse
from datetime import datetime
from collections import defaultdict

# Intentar importar chardet
try:
    import chardet
    HAS_CHARDET = True
except ImportError:
    HAS_CHARDET = False
    print("⚠️  chardet no instalado. Instalar con: pip install chardet")

# ── NORMALIZACIÓN ───────────────────────────────────────────────────────────────
# Mapeo de IDs originales a (tipo_producto, ubicacion, zona)
# Estos IDs vienen de la base de datos anterior mal diseñada
NORMALIZACION = {
    # Sticker products
    17:  ("sticker",    "Salta",          None),
    34:  ("sticker",    "Mar del Plata",  None),
    74:  ("sticker",    "Mendoza",        None),
    135: ("sticker",    "Buenos Aires",   "1"),
    136: ("sticker",    "Buenos Aires",   "2"),
    138: ("sticker",    "Buenos Aires",   "3"),
    139: ("sticker",    "Buenos Aires",   "4"),
    140: ("sticker",    "Córdoba",        None),
    141: ("sticker",    "Tucumán",        None),
    142: ("sticker",    "Bahía Blanca",   None),
    143: ("sticker",    "Santa Fe",       None),
    
    # Backlight products
    146: ("backlight",  "Córdoba",        None),
    169: ("backlight",  "Buenos Aires",   "1"),
    171: ("backlight",  "Bahía Blanca",   None),
    174: ("backlight",  "Buenos Aires",   "2"),
    175: ("backlight",  "Buenos Aires",   "3"),
    176: ("backlight",  "Buenos Aires",   "4"),
    
    # Other products
    151: ("bicicletero","Buenos Aires",   None),
    157: ("sombrilla",  "Buenos Aires",   None),
}

# Productos reales con IDs fijos
PRODUCTOS = {
    "sticker":     1,
    "saliente":    2,
    "backlight":   3,
    "bicicletero": 4,
    "sombrilla":   5,
}

# Ubicaciones reales
UBICACIONES = {
    "Salta": "SAL",
    "Mar del Plata": "MDQ",
    "Mendoza": "MDZ",
    "Buenos Aires": "CABA",
    "Córdoba": "COR",
    "Tucumán": "TUC",
    "Bahía Blanca": "BHI",
    "Santa Fe": "SFE",
}

# Output columns
COLUMNS = [
    "periodo",
    "producto_id",
    "tipo_material",
    "grid",
    "nombre",
    "telefono",
    "direccion",
    "barrio",
    "ciudad",
    "provincia",
    "estado",
    "visitas_realizadas",
    "visita_efectiva",
    "producto_efectivo",
    "logo_actualizado",
    "motivo_de_rechazo",
    "competencia_marca",
    "competencia_material",
    "comentarios",
    "foto1",
    "foto2",
    "fecha",
]


# ── HELPERS ───────────────────────────────────────────────────────────────────

def detect_encoding(filepath):
    """Detecta la codificación del archivo automáticamente"""
    if not HAS_CHARDET:
        return 'latin-1'
    try:
        with open(filepath, 'rb') as f:
            raw = f.read(10000)
            result = chardet.detect(raw)
            return result['encoding'] if result['encoding'] else 'latin-1'
    except Exception:
        return 'latin-1'


def safe(v):
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() in ("nan", "none") else s


def extract_filename(v):
    """Extract filename from HYPERLINK formula or plain name."""
    s = safe(v)
    if not s:
        return ""
    m = re.search(r'["\']([^"\']+\.(?:jpg|jpeg|png|webp))["\']', s, re.IGNORECASE)
    if m:
        return os.path.basename(m.group(1))
    if re.search(r'\.(jpg|jpeg|png|webp)$', s, re.IGNORECASE):
        return os.path.basename(s)
    return ""


def parse_competencia(v):
    """Parse 'Saliente: Rappi.' → ('Rappi', 'Saliente')"""
    s = safe(v)
    if not s or s.lower() == "no":
        return "", ""
    m = re.match(r"([^:]+):\s*(.+?)\.?\s*$", s)
    if m:
        return m.group(2).strip(), m.group(1).strip()
    return s, ""


def norm_sino(v):
    s = safe(v).upper()
    return "SI" if s == "SI" else "NO" if s == "NO" else ""


def leer_csv(filepath):
    """Lee un CSV con encoding automático"""
    encoding = detect_encoding(filepath)
    try:
        with open(filepath, encoding=encoding, errors='replace') as f:
            return f.read()
    except Exception:
        with open(filepath, encoding='latin-1', errors='replace') as f:
            return f.read()


def parse_file(filepath, producto_id_original, periodo=81):
    """
    Lee un CSV original y genera filas normalizadas.
    Para sticker: genera DOS filas (sticker y saliente)
    Para otros: genera UNA fila
    """
    # Obtener tipo real y ubicación del mapeo
    if producto_id_original not in NORMALIZACION:
        print(f"  ⚠️  Producto {producto_id_original} no en NORMALIZACION — omitiendo")
        return []
    
    tipo_material, ubicacion_nombre, zona = NORMALIZACION[producto_id_original]
    producto_id_real = PRODUCTOS[tipo_material]
    
    # Para sticker, también necesitamos el ID de saliente
    saliente_id_real = PRODUCTOS.get("saliente", 2)
    
    # Leer CSV
    content = leer_csv(filepath)
    
    # Detectar separador
    first_line = content.split("\n")[0]
    sep = ";" if first_line.count(";") > first_line.count(",") else ","
    
    reader = csv.DictReader(content.splitlines(), delimiter=sep)
    
    rows_out = []
    
    for row in reader:
        # Normalizar keys
        row = {k.strip().lstrip("\ufeff"): v for k, v in row.items()}
        
        grid = safe(row.get("Grid") or row.get("grid"))
        if not grid:
            continue
        
        nombre = safe(row.get("Nombre") or row.get("nombre"))
        telefono = safe(row.get("Tel") or row.get("telefono"))
        direccion = safe(row.get("Direccion") or row.get("direccion"))
        barrio = safe(row.get("Barrio") or row.get("barrio"))
        ciudad = ubicacion_nombre  # La ciudad viene de la ubicación del producto
        provincia = ""  # Se puede mapear después
        fecha = safe(row.get("Fecha") or row.get("fecha"))
        
        vis_raw = safe(row.get("Vistas_realizadas") or row.get("visitas_realizadas") or "0")
        try:
            vis_int = int(float(vis_raw))
        except Exception:
            vis_int = 0
        
        estado = "Visitado" if vis_int == 1 else "Pendiente"
        visita_efectiva = norm_sino(row.get("Visita_efectiva") or row.get("visita_efectiva"))
        sal_raw = norm_sino(row.get("Saliente_efectivo") or row.get("saliente_efectivo"))
        stk_raw = norm_sino(row.get("Sticker_efectivo") or row.get("sticker_efectivo"))
        motivo = safe(row.get("Motivo") or row.get("motivo_de_rechazo"))
        comentarios = safe(row.get("Comentarios") or row.get("comentarios"))
        
        comp_marca, comp_material = parse_competencia(
            row.get("Competencia") or row.get("competencia") or ""
        )
        
        foto1 = extract_filename(row.get("Foto1") or row.get("foto1"))
        foto2 = extract_filename(row.get("Foto2") or row.get("foto2"))
        
        base = {
            "periodo": periodo,
            "grid": grid,
            "nombre": nombre,
            "telefono": telefono,
            "direccion": direccion,
            "barrio": barrio,
            "ciudad": ciudad,
            "provincia": provincia,
            "estado": estado,
            "visitas_realizadas": vis_int,
            "visita_efectiva": visita_efectiva,
            "motivo_de_rechazo": motivo,
            "competencia_marca": comp_marca,
            "competencia_material": comp_material,
            "comentarios": comentarios,
            "foto1": foto1,
            "foto2": foto2,
            "fecha": fecha,
        }
        
        if tipo_material == "sticker":
            # Generar fila para STICKER
            row_stk = dict(base)
            row_stk["producto_id"] = producto_id_real
            row_stk["tipo_material"] = "sticker"
            row_stk["producto_efectivo"] = stk_raw
            row_stk["logo_actualizado"] = "SI" if stk_raw == "SI" else "NO"
            rows_out.append(row_stk)
            
            # Generar fila para SALIENTE
            row_sal = dict(base)
            row_sal["producto_id"] = saliente_id_real
            row_sal["tipo_material"] = "saliente"
            row_sal["producto_efectivo"] = sal_raw
            row_sal["logo_actualizado"] = "SI" if sal_raw == "SI" else "NO"
            rows_out.append(row_sal)
        else:
            # Backlight, bicicletero, sombrilla
            row_other = dict(base)
            row_other["producto_id"] = producto_id_real
            row_other["tipo_material"] = tipo_material
            producto_efectivo = "SI" if (sal_raw == "SI" or stk_raw == "SI") else "NO"
            row_other["producto_efectivo"] = producto_efectivo
            row_other["logo_actualizado"] = "SI" if producto_efectivo == "SI" else "NO"
            rows_out.append(row_other)
    
    return rows_out


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="POP — Normalizar CSVs a productos reales")
    parser.add_argument("--preview", action="store_true", help="Solo muestra resumen")
    parser.add_argument("--dir", default=".", help="Directorio base")
    parser.add_argument("--periodo", type=int, default=81, help="Periodo")
    args = parser.parse_args()
    
    base_dir = os.path.abspath(args.dir)
    periodo = args.periodo
    output_path = os.path.join(base_dir, f"{periodo}_all.csv")
    
    print(f"\n{'='*70}")
    print(f"  POP — NORMALIZACIÓN DE DATOS")
    print(f"{'='*70}")
    print(f"  Periodo: {periodo}")
    print(f"  Directorio: {base_dir}")
    print(f"  Output: {output_path}")
    print(f"\n  Productos normalizados:")
    for prod, pid in PRODUCTOS.items():
        print(f"    {prod}: ID {pid}")
    print()
    
    # Buscar archivos
    pattern = os.path.join(base_dir, f"{periodo}_*.csv")
    files = sorted(glob.glob(pattern))
    files = [f for f in files if not f.endswith(f"{periodo}_all.csv")]
    
    if not files:
        print(f"❌ No se encontraron archivos {periodo}_*.csv")
        sys.exit(1)
    
    print(f"{'ARCHIVO':<25}  {'ID':>5}  {'TIPO':<12}  {'UBICACIÓN':<18}  {'FILAS':>8}")
    print("─" * 75)
    
    all_rows = []
    productos_procesados = defaultdict(int)
    
    for filepath in files:
        fname = os.path.basename(filepath)
        m = re.match(rf"{periodo}_(\d+)\.csv$", fname, re.IGNORECASE)
        if not m:
            print(f"  ⚠️  Nombre inesperado: {fname}")
            continue
        
        prod_id_original = int(m.group(1))
        
        if prod_id_original not in NORMALIZACION:
            print(f"  ⚠️  Producto {prod_id_original} no reconocido — omitiendo")
            continue
        
        tipo, ubicacion, zona = NORMALIZACION[prod_id_original]
        zona_str = f" Z{zona}" if zona else ""
        rows = parse_file(filepath, prod_id_original, periodo)
        
        all_rows.extend(rows)
        productos_procesados[tipo] += len(rows)
        
        print(f"  {fname:<23}  {prod_id_original:>5}  {tipo:<12}  {ubicacion}{zona_str:<18}  {len(rows):>8}")
    
    print("─" * 75)
    print(f"\n  Total filas generadas: {len(all_rows)}")
    print(f"\n  Desglose por tipo:")
    for tipo, count in sorted(productos_procesados.items()):
        print(f"    {tipo}: {count} filas")
    
    if args.preview:
        print("\n  [PREVIEW] No se escribió nada.\n")
        return
    
    if not all_rows:
        print("\n  ❌ Sin datos para escribir.\n")
        return
    
    # Escribir CSV
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(all_rows)
    
    print(f"\n  ✅ Escrito: {output_path}")
    print(f"  Filas: {len(all_rows)}")
    
    # Mostrar ejemplo
    print(f"\n  Ejemplo de datos generados:")
    for row in all_rows[:3]:
        print(f"    [{row['producto_id']}] {row['tipo_material']} - {row['ciudad']} - efectivo: {row['producto_efectivo']}")
    print()


if __name__ == "__main__":
    main()