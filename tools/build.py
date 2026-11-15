import csv, json, sys
src, tpl, out = sys.argv[1], sys.argv[2], sys.argv[3]
BASE = (sys.argv[4] if len(sys.argv)>4 else "").rstrip("/")
INT = {"diputados","censo_2026","cera_2026","votos_vuelco","ppvox_p5","ppvox_p95"}
FLT = {"vuelco_pts"}
for p in ("pp","psoe","vox","sumar","reg"):
    for s in ("2023","base","prop","prev"):
        INT.add(f"{p}_{s}")
prov = []
for r in csv.DictReader(open(f"{src}/provincias.csv", encoding="utf-8")):
    for k in list(r):
        if k in INT: r[k] = int(r[k])
        elif k in FLT: r[k] = float(r[k])
    prov.append(r)
rang = []
for r in csv.DictReader(open(f"{src}/rangos.csv", encoding="utf-8")):
    r["diputados"] = int(r["diputados"])
    rang.append(r)
data = json.dumps({"prov": prov, "rangos": rang}, ensure_ascii=False, separators=(",", ":"))
html = open(tpl, encoding="utf-8").read().replace("__DATA__", data).replace("__BASE__", BASE)
open(out, "w", encoding="utf-8").write(html)
print(len(prov), len(rang), len(html))
