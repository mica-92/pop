"""
pop_build_db.py  (v4 - Normalizada)
====================================
Crea pop.db con esquema normalizado:
- 5 productos reales (sticker, saliente, backlight, bicicletero, sombrilla)
- Ubicación como atributo del establecimiento
- Una fila por (grid, producto_id, periodo)

Usage:
  python pop_build_db.py                    import 81_all.csv
  python pop_build_db.py --csv 82_all.csv   import other file
  python pop_build_db.py --preview          dry run
  python pop_build_db.py --init             create DB only
  python pop_build_db.py --status           show current state
  python pop_build_db.py --reset            wipe and recreate
"""

import os, sys, csv, sqlite3, argparse
from datetime import datetime
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH  = os.path.join(BASE_DIR, "pop.db")

# Productos reales (normalizados)
PRODUCTOS = {
    1: ("sticker", "Sticker"),
    2: ("saliente", "Saliente"),
    3: ("backlight", "Backlight"),
    4: ("bicicletero", "Bicicletero"),
    5: ("sombrilla", "Sombrilla"),
}

SCHEMA = """
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

CREATE TABLE IF NOT EXISTS chains (
    chain_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre     TEXT NOT NULL UNIQUE,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS establishments (
    grid          TEXT PRIMARY KEY,
    nombre        TEXT,
    telefono      TEXT,
    direccion     TEXT,
    barrio        TEXT,
    ciudad        TEXT,
    provincia     TEXT,
    chain_id      INTEGER REFERENCES chains(chain_id),
    created_at    TEXT DEFAULT (datetime('now')),
    last_modified TEXT DEFAULT (datetime('now')),
    modified_by   TEXT DEFAULT 'import'
);
CREATE INDEX IF NOT EXISTS idx_est_ciudad    ON establishments(ciudad);
CREATE INDEX IF NOT EXISTS idx_est_chain     ON establishments(chain_id);

CREATE TABLE IF NOT EXISTS products (
    producto_id   INTEGER PRIMARY KEY,
    tipo_material TEXT NOT NULL,
    nombre        TEXT,
    descripcion   TEXT
);

CREATE TABLE IF NOT EXISTS visitas (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    grid                 TEXT NOT NULL REFERENCES establishments(grid),
    producto_id          INTEGER NOT NULL REFERENCES products(producto_id),
    periodo              INTEGER NOT NULL,
    estado               TEXT NOT NULL DEFAULT 'Pendiente',
    visitas_realizadas   INTEGER NOT NULL DEFAULT 0,
    visita_efectiva      TEXT,
    producto_efectivo    TEXT,
    logo_actualizado     TEXT,
    motivo_de_rechazo    TEXT,
    competencia_marca    TEXT,
    competencia_material TEXT,
    comentarios          TEXT,
    foto1                TEXT,
    foto2                TEXT,
    fecha                TEXT,
    modified_manually    INTEGER NOT NULL DEFAULT 0,
    last_import          TEXT,
    last_modified        TEXT,
    UNIQUE(grid, producto_id, periodo)
);
CREATE INDEX IF NOT EXISTS idx_vis_grid     ON visitas(grid);
CREATE INDEX IF NOT EXISTS idx_vis_periodo  ON visitas(periodo);
CREATE INDEX IF NOT EXISTS idx_vis_producto ON visitas(producto_id);
CREATE INDEX IF NOT EXISTS idx_vis_estado   ON visitas(estado);

CREATE TABLE IF NOT EXISTS log (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp     TEXT NOT NULL DEFAULT (datetime('now')),
    tipo          TEXT NOT NULL,
    accion        TEXT NOT NULL,
    grid          TEXT,
    producto_id   INTEGER,
    periodo       INTEGER,
    campo         TEXT,
    val_antes     TEXT,
    val_desp      TEXT,
    detalle       TEXT
);
CREATE INDEX IF NOT EXISTS idx_log_ts   ON log(timestamp);
CREATE INDEX IF NOT EXISTS idx_log_grid ON log(grid);
"""

KNOWN_CHAINS = [
    "CARREFOUR","FREDDO","GRIDO","MOSTAZA","DIA","365 KIOSCO","SUBWAY",
    "BROZZIANO","TERCERA DOCENA","MANDALEFRUTA","TEMPLE BURGER",
    "KIOSCOS THE BEST","MAS FARMACIA","LA JUVENIL","LA PAYADA",
    "EL CLUB DE LA MILANESA","CASAPAN","WHITE SHARK","SUSHI SENSEI",
    "FABRIC SUSHI","PANCHOS RICKY","RIVIERA HELADOS","FOREST DAN",
    "EMILY DANIELS","TIENDA DE CAFE","GLACE HELADOS","CHUNGO",
]
CHAIN_PREFIXES = sorted(KNOWN_CHAINS, key=len, reverse=True)

def detect_chain(nombre):
    if not nombre: return None
    n = nombre.upper()
    for c in CHAIN_PREFIXES:
        if n.startswith(c) or f" {c}" in n:
            return c.strip()
    return None

def get_conn():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    con.execute("PRAGMA encoding = 'UTF-8'")
    return con

def safe(v):
    if v is None: return None
    s = str(v).strip()
    return None if s.lower() in ("","nan","none") else s

def safe_int(v):
    try: return int(float(str(v).strip()))
    except: return 0

def init_db():
    """Initialize database with products"""
    con = get_conn()
    con.executescript(SCHEMA)
    
    for pid, (tipo, nombre) in PRODUCTOS.items():
        con.execute("INSERT OR IGNORE INTO products(producto_id, tipo_material, nombre) VALUES(?,?,?)",
                    (pid, tipo, nombre))
    
    con.commit()
    con.close()
    print(f"✅ DB inicializada: {DB_PATH}")
    print(f"   {len(PRODUCTOS)} productos cargados")
    for pid, (tipo, nombre) in PRODUCTOS.items():
        print(f"     {pid}: {nombre} ({tipo})")

def import_csv(csv_path, dry_run=False):
    """Import CSV with normalized structure"""
    print(f"\n{'[DRY-RUN] ' if dry_run else ''}Importando: {csv_path}\n")
    
    if not os.path.exists(csv_path):
        print(f"❌ No se encontro: {csv_path}")
        sys.exit(1)
    
    with open(csv_path, encoding="utf-8-sig", errors="replace") as f:
        rows = list(csv.DictReader(f))
    
    print(f"  📄 Filas en CSV: {len(rows)}")
    
    con = get_conn()
    ts = datetime.now().isoformat()
    
    existing_est = {r[0] for r in con.execute("SELECT grid FROM establishments").fetchall()}
    existing_vis = {}
    for r in con.execute("SELECT grid, producto_id, periodo, modified_manually FROM visitas").fetchall():
        existing_vis[(r[0], int(r[1]), int(r[2]))] = r[3]
    
    existing_chains = {r[0]: r[1] for r in con.execute("SELECT nombre, chain_id FROM chains").fetchall()}
    
    stats = {"est_new": 0, "est_skip": 0, "vis_ins": 0, "vis_upd": 0, "vis_skip": 0, "err": 0}
    productos_stats = defaultdict(int)
    
    for row in rows:
        try:
            grid = safe(row.get("grid"))
            producto_id = safe_int(row.get("producto_id"))
            periodo = safe_int(row.get("periodo") or 81)
            
            if not grid or not producto_id:
                stats["err"] += 1
                continue
            
            nombre = safe(row.get("nombre"))
            telefono = safe(row.get("telefono"))
            direccion = safe(row.get("direccion"))
            barrio = safe(row.get("barrio"))
            ciudad = safe(row.get("ciudad"))
            provincia = safe(row.get("provincia"))
            fecha = safe(row.get("fecha"))
            
            estado = safe(row.get("estado")) or "Pendiente"
            visitas_realizadas = safe_int(row.get("visitas_realizadas"))
            visita_efectiva = safe(row.get("visita_efectiva"))
            producto_efectivo = safe(row.get("producto_efectivo"))
            logo_actualizado = safe(row.get("logo_actualizado"))
            motivo = safe(row.get("motivo_de_rechazo"))
            comp_marca = safe(row.get("competencia_marca"))
            comp_material = safe(row.get("competencia_material"))
            comentarios = safe(row.get("comentarios"))
            foto1 = safe(row.get("foto1"))
            foto2 = safe(row.get("foto2"))
            
            productos_stats[producto_id] += 1
            
            # Establishments
            if grid not in existing_est:
                chain_name = detect_chain(nombre)
                chain_id = None
                if chain_name:
                    if chain_name not in existing_chains:
                        if not dry_run:
                            cur = con.execute("INSERT OR IGNORE INTO chains(nombre) VALUES(?)", (chain_name,))
                            chain_id = cur.lastrowid or con.execute(
                                "SELECT chain_id FROM chains WHERE nombre=?", (chain_name,)
                            ).fetchone()[0]
                            existing_chains[chain_name] = chain_id
                        else:
                            chain_id = -1
                    else:
                        chain_id = existing_chains[chain_name]
                
                if not dry_run:
                    con.execute("""
                        INSERT OR IGNORE INTO establishments 
                        (grid, nombre, telefono, direccion, barrio, ciudad, provincia, chain_id) 
                        VALUES(?,?,?,?,?,?,?,?)
                    """, (grid, nombre, telefono, direccion, barrio, ciudad, provincia, chain_id))
                
                existing_est.add(grid)
                stats["est_new"] += 1
            else:
                stats["est_skip"] += 1
            
            # Visitas
            key = (grid, producto_id, periodo)
            
            if key not in existing_vis:
                if not dry_run:
                    con.execute("""
                        INSERT INTO visitas(
                            grid, producto_id, periodo, estado, visitas_realizadas,
                            visita_efectiva, producto_efectivo, logo_actualizado,
                            motivo_de_rechazo, competencia_marca, competencia_material,
                            comentarios, foto1, foto2, fecha,
                            modified_manually, last_import, last_modified
                        ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,?,?)
                    """, (
                        grid, producto_id, periodo, estado, visitas_realizadas,
                        visita_efectiva, producto_efectivo, logo_actualizado,
                        motivo, comp_marca, comp_material,
                        comentarios, foto1, foto2, fecha,
                        ts, ts
                    ))
                stats["vis_ins"] += 1
            else:
                if existing_vis[key] == 1:
                    stats["vis_skip"] += 1
                    continue
                
                if not dry_run:
                    con.execute("""
                        UPDATE visitas SET 
                            estado=?, visitas_realizadas=?,
                            visita_efectiva=?, producto_efectivo=?, logo_actualizado=?,
                            motivo_de_rechazo=?, competencia_marca=?, competencia_material=?,
                            comentarios=?, foto1=?, foto2=?, fecha=?,
                            last_import=?, modified_manually=0
                        WHERE grid=? AND producto_id=? AND periodo=?
                    """, (
                        estado, visitas_realizadas,
                        visita_efectiva, producto_efectivo, logo_actualizado,
                        motivo, comp_marca, comp_material,
                        comentarios, foto1, foto2, fecha,
                        ts, grid, producto_id, periodo
                    ))
                stats["vis_upd"] += 1
                
        except Exception as e:
            print(f"  ❌ Error: {e}")
            stats["err"] += 1
    
    if not dry_run:
        con.commit()
    con.close()
    
    print(f"\n  📊 Resumen:")
    print(f"  {'─'*40}")
    print(f"  Establecimientos nuevos:   {stats['est_new']}")
    print(f"  Establecimientos exist.:   {stats['est_skip']}")
    print(f"  Visitas insertadas:        {stats['vis_ins']}")
    print(f"  Visitas actualizadas:      {stats['vis_upd']}")
    print(f"  Saltadas (manuales):       {stats['vis_skip']}")
    print(f"  Errores:                   {stats['err']}")
    
    if dry_run:
        print("\n  [DRY-RUN] Nada modificado.\n")

def show_status():
    if not os.path.exists(DB_PATH):
        print(f"❌ No existe: {DB_PATH}")
        return
    
    con = get_conn()
    print(f"\n{'='*60}")
    print(f"  POP DB STATUS (Normalizado)")
    print(f"{'='*60}")
    
    n_est = con.execute("SELECT COUNT(*) FROM establishments").fetchone()[0]
    n_ch = con.execute("SELECT COUNT(*) FROM chains").fetchone()[0]
    total = con.execute("SELECT COUNT(*) FROM visitas").fetchone()[0]
    vis = con.execute("SELECT COUNT(*) FROM visitas WHERE estado='Visitado'").fetchone()[0]
    
    print(f"\n  📍 Establecimientos: {n_est}")
    print(f"  🔗 Cadenas: {n_ch}")
    print(f"  📋 Visitas totales: {total}")
    print(f"     ✓ Visitadas: {vis} ({round(vis/total*100,1) if total else 0}%)")
    print(f"     · Pendientes: {total - vis}")
    
    print(f"\n  📊 Por producto:")
    print(f"  {'─'*50}")
    for pid, (tipo, nombre) in PRODUCTOS.items():
        stats = con.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN v.estado='Visitado' THEN 1 ELSE 0 END) as visitados,
                SUM(CASE WHEN v.producto_efectivo='SI' THEN 1 ELSE 0 END) as efectivo
            FROM visitas v
            WHERE v.producto_id = ?
        """, (pid,)).fetchone()
        
        if stats['total'] > 0:
            pct = round(stats['visitados']/stats['total']*100, 1) if stats['total'] else 0
            print(f"  {nombre:<15} {stats['total']:>6} visitas, {stats['visitados']:>5} visitadas ({pct}%)")
    
    print(f"\n  🗺️  Por ciudad:")
    for r in con.execute("""
        SELECT ciudad, COUNT(*) as total
        FROM establishments
        GROUP BY ciudad
        ORDER BY total DESC
        LIMIT 5
    """).fetchall():
        print(f"    {r['ciudad']}: {r['total']} locales")
    
    print(f"\n{'='*60}\n")
    con.close()

def main():
    parser = argparse.ArgumentParser(description="POP — Build DB (Normalizado)")
    parser.add_argument("--csv", default="81_all.csv")
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--init", action="store_true")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    
    if args.reset:
        confirm = input(f"⚠️  BORRAR {DB_PATH}? [s/N] ").strip().lower()
        if confirm == "s":
            if os.path.exists(DB_PATH):
                os.remove(DB_PATH)
            init_db()
        return
    
    if args.init:
        if not os.path.exists(DB_PATH):
            init_db()
        else:
            confirm = input(f"⚠️  Ya existe. ¿Reinicializar? [s/N] ").strip().lower()
            if confirm == "s":
                os.remove(DB_PATH)
                init_db()
        return
    
    if args.status:
        show_status()
        return
    
    if not os.path.exists(DB_PATH):
        print("⚠️  DB no encontrada — inicializando...")
        init_db()
    
    csv_path = os.path.join(BASE_DIR, args.csv)
    import_csv(csv_path, dry_run=args.preview)
    
    if not args.preview:
        show_status()

if __name__ == "__main__":
    main()