import csv, json, sys
src, tpl, out = sys.argv[1], sys.argv[2], sys.argv[3]
BASE = (sys.argv[4] if len(sys.argv)>4 else "").rstrip("/")
VEDA = len(sys.argv)>5 and sys.argv[5]=="--veda"
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
if VEDA:
    keep = {"comunidad","provincia","diputados","censo_2026","cera_2026"}
    keep |= {k for k in prov[0] if k.endswith("_2023")}
    prov = [{k:v for k,v in r.items() if k in keep} for r in prov]
    rang = []
data = json.dumps({"prov": prov, "rangos": rang}, ensure_ascii=False, separators=(",", ":"))
html = open(tpl, encoding="utf-8").read().replace("__DATA__", data).replace("__BASE__", BASE)
if VEDA:
    old = "var vedado=Date.now()>=VEDA_FROM || location.hash===\"#veda\";"
    assert old in html
    html = html.replace(old, "var vedado=true;")
open(out, "w", encoding="utf-8").write(html)
print(len(prov), len(rang), len(html))
