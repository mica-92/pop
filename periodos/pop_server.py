"""
pop_server.py — POP Dashboard Flask server (v4 - Normalizado)
Run: python pop_server.py
"""

import os, sys, sqlite3
from datetime import datetime
from collections import defaultdict
from flask import Flask, request, jsonify, Response, send_from_directory

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
DB_PATH   = os.path.join(BASE_DIR, "pop.db")
HTML_PATH = os.path.join(BASE_DIR, "pop_app.html")
IMG_DIR   = os.path.join(BASE_DIR, "images")
PORT      = int(sys.argv[sys.argv.index("--port")+1]) if "--port" in sys.argv else 5000

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys=ON")
    return con

def q(sql, params=()):
    con = get_db()
    rows = con.execute(sql, params).fetchall()
    con.close()
    return [dict(r) for r in rows]

def q1(sql, params=()):
    con = get_db()
    row = con.execute(sql, params).fetchone()
    con.close()
    return dict(row) if row else None

@app.route("/")
def index():
    if os.path.exists(HTML_PATH):
        with open(HTML_PATH, encoding="utf-8") as f:
            return Response(f.read(), mimetype="text/html; charset=utf-8")
    return Response("<h1>pop_app.html not found</h1>", status=404, mimetype="text/html")

@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(IMG_DIR, filename)

@app.after_request
def cors(r):
    r.headers["Access-Control-Allow-Origin"] = "*"
    r.headers["Access-Control-Allow-Headers"] = "Content-Type"
    r.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return r

def parse_periodos(param):
    if not param or param.strip().lower() in ("", "all"):
        return [r["periodo"] for r in q("SELECT DISTINCT periodo FROM visitas ORDER BY periodo")]
    try:
        return sorted(set(int(p.strip()) for p in param.split(",") if p.strip()))
    except:
        return []

def pclause(periodos):
    if not periodos:
        return "1=1", []
    return f"v.periodo IN ({','.join('?' * len(periodos))})", list(periodos)

def stats(rows):
    total = len(rows)
    vis = sum(1 for r in rows if r.get("estado") == "Visitado")
    efec = sum(1 for r in rows if r.get("visita_efectiva") == "SI")
    producto_ef = sum(1 for r in rows if r.get("producto_efectivo") == "SI")
    logo = sum(1 for r in rows if r.get("logo_actualizado") == "SI")
    comp = sum(1 for r in rows if r.get("competencia_marca"))
    no_ef = sum(1 for r in rows if r.get("visita_efectiva") == "NO")
    return {
        "total": total,
        "visitados": vis,
        "pendientes": total - vis,
        "efectivos": efec,
        "producto_efectivo": producto_ef,
        "no_efectivos": no_ef,
        "logo_ok": logo,
        "competencia": comp,
        "pct_visitados": round(vis / total * 100, 1) if total else 0,
        "pct_efectivos": round(efec / vis * 100, 1) if vis else 0,
        "pct_logo": round(logo / vis * 100, 1) if vis else 0
    }

@app.route("/api/periodos")
def api_periodos():
    return jsonify(q("""
        SELECT v.periodo, COUNT(*) as total,
            SUM(CASE WHEN v.estado='Visitado' THEN 1 ELSE 0 END) as visitados,
            SUM(CASE WHEN v.estado='Pendiente' THEN 1 ELSE 0 END) as pendientes,
            MIN(v.fecha) as fecha_min, MAX(v.fecha) as fecha_max
        FROM visitas v
        GROUP BY v.periodo
        ORDER BY v.periodo DESC
    """))

@app.route("/api/stats")
def api_stats():
    pc, pp = pclause(parse_periodos(request.args.get("periodo", "")))
    rows = q(f"""
        SELECT v.estado, v.visita_efectiva, v.producto_efectivo, v.logo_actualizado, v.competencia_marca
        FROM visitas v
        WHERE {pc}
    """, pp)
    return jsonify(stats(rows))

@app.route("/api/products")
def api_products():
    pc, pp = pclause(parse_periodos(request.args.get("periodo", "")))
    rows = q(f"""
        SELECT v.producto_id, p.tipo_material, p.nombre as producto_nombre,
            v.estado, v.visita_efectiva, v.producto_efectivo, v.logo_actualizado,
            v.competencia_marca, v.motivo_de_rechazo
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        WHERE {pc}
    """, pp)
    
    grouped = {}
    for r in rows:
        pid = r["producto_id"]
        if pid not in grouped:
            grouped[pid] = {
                "producto_id": pid,
                "tipo_material": r["tipo_material"],
                "producto_nombre": r["producto_nombre"],
                "rows": []
            }
        grouped[pid]["rows"].append(r)
    
    result = []
    for pid, d in sorted(grouped.items()):
        s = stats(d["rows"])
        motivos = defaultdict(int)
        for r in d["rows"]:
            if r.get("motivo_de_rechazo"):
                motivos[r["motivo_de_rechazo"]] += 1
        result.append({
            "producto_id": pid,
            "tipo_material": d["tipo_material"],
            "producto_nombre": d["producto_nombre"],
            "motivos": dict(sorted(motivos.items(), key=lambda x: -x[1])),
            **s
        })
    return jsonify(result)

@app.route("/api/geography")
def api_geography():
    pc, pp = pclause(parse_periodos(request.args.get("periodo", "")))
    rows = q(f"""
        SELECT e.ciudad, v.producto_id, p.tipo_material, v.estado,
            v.visita_efectiva, v.producto_efectivo, v.logo_actualizado, v.competencia_marca
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        JOIN establishments e ON v.grid = e.grid
        WHERE {pc}
    """, pp)
    
    grouped = {}
    for r in rows:
        ciudad = r["ciudad"] or "Otra"
        if ciudad not in grouped:
            grouped[ciudad] = {"ciudad": ciudad, "rows": [], "productos": set()}
        grouped[ciudad]["rows"].append(r)
        grouped[ciudad]["productos"].add(r["producto_id"])
    
    return jsonify([{
        "ciudad": d["ciudad"],
        "n_productos": len(d["productos"]),
        **stats(d["rows"])
    } for ciudad, d in sorted(grouped.items())])

@app.route("/api/visitas")
def api_visitas():
    pc, params = pclause(parse_periodos(request.args.get("periodo", "")))
    where = [pc]
    
    for arg, col in [
        ("producto", "v.producto_id"),
        ("ciudad", "e.ciudad"),
        ("estado", "v.estado"),
        ("tipo", "p.tipo_material"),
        ("grid", "v.grid"),
        ("chain_id", "e.chain_id")
    ]:
        val = request.args.get(arg)
        if val:
            where.append(f"{col}=?")
            params.append(int(val) if arg in ("producto", "chain_id") else val)
    
    qt = request.args.get("q", "").strip().lower()
    if qt:
        where.append("(LOWER(e.nombre) LIKE ? OR v.grid LIKE ? OR LOWER(e.barrio) LIKE ?)")
        params += [f"%{qt}%"] * 3
    
    limit = int(request.args.get("limit", 500))
    offset = int(request.args.get("offset", 0))
    ws = " AND ".join(where)
    
    total = q1(f"""
        SELECT COUNT(*) as n
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        JOIN establishments e ON v.grid = e.grid
        WHERE {ws}
    """, params)["n"]
    
    rows = q(f"""
        SELECT v.id, v.grid, v.producto_id, v.periodo,
            p.tipo_material, p.nombre as producto_nombre,
            e.nombre, e.telefono, e.direccion, e.barrio, e.ciudad, e.provincia,
            e.chain_id, c.nombre as cadena,
            v.estado, v.visitas_realizadas,
            v.visita_efectiva, v.producto_efectivo, v.logo_actualizado,
            v.motivo_de_rechazo, v.competencia_marca, v.competencia_material, v.comentarios,
            v.foto1, v.foto2, v.fecha, v.modified_manually, v.last_modified
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        JOIN establishments e ON v.grid = e.grid
        LEFT JOIN chains c ON e.chain_id = c.chain_id
        WHERE {ws}
        ORDER BY e.nombre, v.producto_id
        LIMIT ? OFFSET ?
    """, params + [limit, offset])
    
    return jsonify({"total": total, "rows": rows, "limit": limit, "offset": offset})

@app.route("/api/visita/<int:vid>", methods=["GET"])
def api_visita_get(vid):
    row = q1("""
        SELECT v.*, e.nombre, e.telefono, e.direccion, e.barrio, e.ciudad, e.provincia,
            e.chain_id, c.nombre as cadena,
            p.tipo_material, p.nombre as producto_nombre
        FROM visitas v
        JOIN establishments e ON v.grid = e.grid
        LEFT JOIN chains c ON e.chain_id = c.chain_id
        JOIN products p ON v.producto_id = p.producto_id
        WHERE v.id = ?
    """, (vid,))
    return jsonify(row) if row else (jsonify({"error": "not found"}), 404)

@app.route("/api/visita/<int:vid>", methods=["PUT", "OPTIONS"])
def api_visita_put(vid):
    if request.method == "OPTIONS":
        return "", 204
    
    data = request.json or {}
    allowed = {"visita_efectiva", "producto_efectivo", "logo_actualizado", "motivo_de_rechazo",
               "competencia_marca", "competencia_material", "comentarios", "estado"}
    updates = {k: v for k, v in data.items() if k in allowed}
    
    if not updates:
        return jsonify({"error": "no valid fields"}), 400
    
    con = get_db()
    row = con.execute("SELECT * FROM visitas WHERE id=?", (vid,)).fetchone()
    if not row:
        con.close()
        return jsonify({"error": "not found"}), 404
    
    row = dict(row)
    ts = datetime.now().isoformat()
    
    for campo, val in updates.items():
        if str(row.get(campo)) != str(val):
            con.execute("""
                INSERT INTO log(tipo, accion, grid, producto_id, periodo, campo, val_antes, val_desp, detalle)
                VALUES('MANUAL', 'visita_edit', ?, ?, ?, ?, ?, ?, 'dashboard')
            """, (row["grid"], row["producto_id"], row["periodo"], campo, str(row.get(campo)), str(val)))
    
    sc = ", ".join(f"{k}=?" for k in updates)
    con.execute(f"UPDATE visitas SET {sc}, modified_manually=1, last_modified=? WHERE id=?",
                list(updates.values()) + [ts, vid])
    con.commit()
    con.close()
    return jsonify({"ok": True})

@app.route("/api/establishments")
def api_establishments():
    where, params = ["1=1"], []
    
    qt = request.args.get("q", "").strip().lower()
    if qt:
        where.append("(LOWER(e.nombre) LIKE ? OR e.grid LIKE ? OR LOWER(e.ciudad) LIKE ?)")
        params += [f"%{qt}%"] * 3
    
    if request.args.get("chain_id"):
        where.append("e.chain_id=?")
        params.append(int(request.args["chain_id"]))
    
    limit = int(request.args.get("limit", 500))
    offset = int(request.args.get("offset", 0))
    ws = " AND ".join(where)
    
    total = q1(f"SELECT COUNT(*) as n FROM establishments e WHERE {ws}", params)["n"]
    
    rows = q(f"""
        SELECT e.grid, e.nombre, e.telefono, e.direccion, e.barrio, e.ciudad, e.provincia,
            e.chain_id, c.nombre as cadena, e.last_modified,
            COUNT(DISTINCT v.producto_id) as n_productos,
            SUM(CASE WHEN v.estado='Visitado' THEN 1 ELSE 0 END) as visitados,
            SUM(CASE WHEN v.estado='Pendiente' THEN 1 ELSE 0 END) as pendientes
        FROM establishments e
        LEFT JOIN chains c ON e.chain_id = c.chain_id
        LEFT JOIN visitas v ON e.grid = v.grid
        WHERE {ws}
        GROUP BY e.grid
        ORDER BY e.nombre
        LIMIT ? OFFSET ?
    """, params + [limit, offset])
    
    return jsonify({"total": total, "rows": rows})

@app.route("/api/establishment/<grid>", methods=["GET"])
def api_establishment_get(grid):
    est = q1("""
        SELECT e.*, c.nombre as cadena
        FROM establishments e
        LEFT JOIN chains c ON e.chain_id = c.chain_id
        WHERE e.grid = ?
    """, (grid,))
    
    if not est:
        return jsonify({"error": "not found"}), 404
    
    visits = q("""
        SELECT v.id, v.producto_id, v.periodo,
            p.tipo_material, p.nombre as producto_nombre,
            v.estado, v.visita_efectiva, v.producto_efectivo, v.logo_actualizado,
            v.motivo_de_rechazo, v.competencia_marca, v.competencia_material, v.comentarios,
            v.foto1, v.foto2, v.fecha, v.modified_manually
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        WHERE v.grid = ?
        ORDER BY v.periodo DESC, v.producto_id
    """, (grid,))
    
    return jsonify({**est, "visitas": visits})

@app.route("/api/establishment/<grid>", methods=["PUT", "OPTIONS"])
def api_establishment_put(grid):
    if request.method == "OPTIONS":
        return "", 204
    
    data = request.json or {}
    allowed = {"nombre", "telefono", "direccion", "barrio", "ciudad", "provincia", "chain_id"}
    updates = {k: v for k, v in data.items() if k in allowed}
    
    if not updates:
        return jsonify({"error": "no valid fields"}), 400
    
    con = get_db()
    est = con.execute("SELECT * FROM establishments WHERE grid=?", (grid,)).fetchone()
    if not est:
        con.close()
        return jsonify({"error": "not found"}), 404
    
    est = dict(est)
    ts = datetime.now().isoformat()
    
    for campo, val in updates.items():
        if str(est.get(campo)) != str(val):
            con.execute("""
                INSERT INTO log(tipo, accion, grid, campo, val_antes, val_desp, detalle)
                VALUES('MANUAL', 'est_edit', ?, ?, ?, ?, 'dashboard')
            """, (grid, campo, str(est.get(campo)), str(val)))
    
    sc = ", ".join(f"{k}=?" for k in updates)
    con.execute(f"UPDATE establishments SET {sc}, last_modified=?, modified_by='dashboard' WHERE grid=?",
                list(updates.values()) + [ts, grid])
    con.commit()
    con.close()
    return jsonify({"ok": True})

@app.route("/api/chains")
def api_chains():
    return jsonify(q("""
        SELECT c.chain_id, c.nombre,
            COUNT(DISTINCT e.grid) as n_establecimientos,
            COUNT(v.id) as total_visitas,
            SUM(CASE WHEN v.estado='Visitado' THEN 1 ELSE 0 END) as visitados,
            SUM(CASE WHEN v.estado='Pendiente' THEN 1 ELSE 0 END) as pendientes
        FROM chains c
        LEFT JOIN establishments e ON c.chain_id = e.chain_id
        LEFT JOIN visitas v ON e.grid = v.grid
        GROUP BY c.chain_id
        ORDER BY n_establecimientos DESC
    """))

@app.route("/api/chains", methods=["POST"])
def api_chains_post():
    nombre = ((request.json or {}).get("nombre") or "").strip().upper()
    if not nombre:
        return jsonify({"error": "nombre requerido"}), 400
    
    con = get_db()
    cur = con.execute("INSERT OR IGNORE INTO chains(nombre) VALUES(?)", (nombre,))
    con.commit()
    cid = cur.lastrowid or con.execute("SELECT chain_id FROM chains WHERE nombre=?", (nombre,)).fetchone()[0]
    con.close()
    return jsonify({"ok": True, "chain_id": cid})

@app.route("/api/chain/<int:chain_id>/assign", methods=["POST", "OPTIONS"])
def api_chain_assign(chain_id):
    if request.method == "OPTIONS":
        return "", 204
    
    grids = (request.json or {}).get("grids", [])
    if not grids:
        return jsonify({"error": "grids requerido"}), 400
    
    con = get_db()
    ts = datetime.now().isoformat()
    upd = 0
    
    for grid in grids:
        if con.execute("SELECT 1 FROM establishments WHERE grid=?", (grid,)).fetchone():
            con.execute("""
                UPDATE establishments
                SET chain_id=?, last_modified=?, modified_by='dashboard'
                WHERE grid=?
            """, (chain_id, ts, grid))
            upd += 1
    
    con.commit()
    con.close()
    return jsonify({"ok": True, "updated": upd})

@app.route("/api/log")
def api_log():
    where, params = ["1=1"], []
    
    for arg, col in [("grid", "grid"), ("tipo", "tipo"), ("periodo", "periodo"), ("producto", "producto_id")]:
        val = request.args.get(arg)
        if val:
            where.append(f"{col}=?")
            params.append(int(val) if arg in ("periodo", "producto") else val)
    
    limit = int(request.args.get("limit", 200))
    return jsonify(q(f"""
        SELECT * FROM log
        WHERE {' AND '.join(where)}
        ORDER BY id DESC
        LIMIT ?
    """, params + [limit]))

@app.route("/api/report")
def api_report():
    periodos = parse_periodos(request.args.get("periodo", ""))
    tipo_rpt = request.args.get("tipo", "general").lower()
    pc, params = pclause(periodos)
    where = [pc]
    
    for arg, col in [
        ("producto", "v.producto_id"),
        ("ciudad", "e.ciudad"),
        ("estado", "v.estado"),
        ("chain_id", "e.chain_id"),
        ("tipo", "p.tipo_material")
    ]:
        val = request.args.get(arg)
        if val:
            where.append(f"{col}=?")
            params.append(int(val) if arg in ("producto", "chain_id") else val)
    
    if request.args.get("fecha_desde"):
        where.append("v.fecha>=?")
        params.append(request.args["fecha_desde"])
    if request.args.get("fecha_hasta"):
        where.append("v.fecha<=?")
        params.append(request.args["fecha_hasta"])
    
    rows = q(f"""
        SELECT v.grid, v.producto_id, v.periodo,
            p.tipo_material, p.nombre as producto_nombre,
            e.nombre, e.direccion, e.barrio, e.ciudad, e.provincia, c.nombre as cadena,
            v.estado, v.visita_efectiva, v.producto_efectivo, v.logo_actualizado,
            v.motivo_de_rechazo, v.competencia_marca, v.competencia_material, v.comentarios,
            v.foto1, v.foto2, v.fecha
        FROM visitas v
        JOIN products p ON v.producto_id = p.producto_id
        JOIN establishments e ON v.grid = e.grid
        LEFT JOIN chains c ON e.chain_id = c.chain_id
        WHERE {' AND '.join(where)}
        ORDER BY e.ciudad, e.nombre, v.producto_id
    """, params)
    
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    pstr = ", ".join(map(str, periodos)) if periodos else "todos"
    W = 72
    sep = "─" * W
    sep2 = "═" * W
    s = stats(rows)
    
    lines = [
        sep2,
        f"  POP — REPORTE DE AUDITORÍA",
        f"  Período(s): {pstr}   |   Tipo: {tipo_rpt.upper()}",
        f"  Generado:   {now}",
        sep2,
        "",
        "  RESUMEN GENERAL",
        sep,
        f"  {'Total locales':<35} {s['total']:>6}",
        f"  {'Visitados':<35} {s['visitados']:>6}  ({s['pct_visitados']}%)",
        f"  {'Pendientes':<35} {s['pendientes']:>6}",
        f"  {'Visitas efectivas':<35} {s['efectivos']:>6}  ({s['pct_efectivos']}% de visitados)",
        f"  {'Producto presente':<35} {s['producto_efectivo']:>6}",
        f"  {'Logo actualizado':<35} {s['logo_ok']:>6}",
        f"  {'Con competencia':<35} {s['competencia']:>6}",
        ""
    ]
    
    if tipo_rpt in ("general", "producto", "product"):
        by_prod = defaultdict(list)
        for r in rows:
            by_prod[(r["producto_id"], r["tipo_material"], r["producto_nombre"])].append(r)
        
        lines += ["  POR PRODUCTO", sep]
        for (pid, tipo, nombre), rr in sorted(by_prod.items()):
            vis = sum(1 for r in rr if r["estado"] == "Visitado")
            pct = round(vis / len(rr) * 100, 1) if rr else 0
            ef = sum(1 for r in rr if r["visita_efectiva"] == "SI")
            prod_ef = sum(1 for r in rr if r["producto_efectivo"] == "SI")
            lines += [
                f"\n  [{pid}] {nombre.upper()}",
                "  " + "─" * 40,
                f"  Total: {len(rr)}  Visitados: {vis} ({pct}%)  Efectivos: {ef}  Producto OK: {prod_ef}"
            ]
            for r in sorted(rr, key=lambda x: x["nombre"] or ""):
                est = "✓" if r["estado"] == "Visitado" else "·"
                ef_c = "EF" if r["visita_efectiva"] == "SI" else "  "
                prod_c = "P" if r["producto_efectivo"] == "SI" else " "
                logo = "L" if r["logo_actualizado"] == "SI" else " "
                ciudad = f"[{r['ciudad']}]" if r.get("ciudad") else ""
                lines.append(f"    {est} {ef_c} {prod_c} {logo}  {(r['nombre'] or '')[:35]:<35} {ciudad}")
    
    elif tipo_rpt in ("geografia", "geography", "geo"):
        by_ciudad = defaultdict(list)
        for r in rows:
            ciudad = r["ciudad"] or "Otra"
            by_ciudad[ciudad].append(r)
        
        lines += ["  POR GEOGRAFÍA", sep]
        for ciudad, rr in sorted(by_ciudad.items()):
            vis = sum(1 for r in rr if r["estado"] == "Visitado")
            pct = round(vis / len(rr) * 100, 1) if rr else 0
            lines += [f"\n  ▌ {ciudad}  —  {len(rr)} locales  |  {vis} visitados ({pct}%)", "  " + "─" * 50]
            for r in sorted(rr, key=lambda x: x["nombre"] or ""):
                est = "✓" if r["estado"] == "Visitado" else "·"
                ef_c = "ef" if r["visita_efectiva"] == "SI" else "  "
                prod_c = "p" if r["producto_efectivo"] == "SI" else " "
                logo = "L" if r["logo_actualizado"] == "SI" else " "
                lines.append(f"    {est}  {(r['nombre'] or '')[:44]:<44}  {ef_c}{prod_c}{logo}")
    
    elif tipo_rpt in ("pendientes", "pending"):
        pending = [r for r in rows if r["estado"] == "Pendiente"]
        by_ciudad = defaultdict(list)
        for r in pending:
            ciudad = r["ciudad"] or "Otra"
            by_ciudad[ciudad].append(r)
        
        lines += [f"  LOCALES PENDIENTES ({len(pending)} total)", sep]
        for ciudad, rr in sorted(by_ciudad.items()):
            lines.append(f"\n  ▌ {ciudad}")
            for r in sorted(rr, key=lambda x: x["nombre"] or ""):
                prod = f"[{r['producto_nombre']}]" if r.get("producto_nombre") else ""
                lines.append(f"    · {(r['nombre'] or '')[:40]:<40}  {prod}")
    
    elif tipo_rpt in ("competencia", "competition"):
        comp_rows = [r for r in rows if r.get("competencia_marca")]
        by_marca = defaultdict(list)
        for r in comp_rows:
            by_marca[r["competencia_marca"]].append(r)
        
        lines += [f"  COMPETENCIA DETECTADA ({len(comp_rows)} locales)", sep]
        for marca, rr in sorted(by_marca.items(), key=lambda x: -len(x[1])):
            lines.append(f"\n  ▌ {marca} ({len(rr)} locales)")
            for r in sorted(rr, key=lambda x: x["nombre"] or ""):
                mat = r.get("competencia_material") or ""
                ciudad = r.get("ciudad") or ""
                lines.append(f"    · {(r['nombre'] or '')[:40]:<40}  {mat:<10}  [{ciudad}]")
    
    lines += ["", sep2, ""]
    content = "\n".join(lines)
    fname = f"POP_{tipo_rpt}_p{pstr.replace(', ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    
    return Response(
        content,
        mimetype="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename={fname}"}
    )

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print(f"No se encontro {DB_PATH}\nEjecuta: python pop_build_db.py")
        sys.exit(1)
    print(f"\n── POP Server  http://localhost:{PORT} ──\n")
    app.run(port=PORT, debug=True, host="0.0.0.0")