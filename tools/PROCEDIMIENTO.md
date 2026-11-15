# Regenerar la web (29N: el escaño en el aire)

1. Sustituir `tools/data/provincias.csv` y `tools/data/rangos.csv` por los datasets actuales del panel «Análisis electoral 29-N» (mismas columnas).
2. Desde la raíz del repositorio:
   `python3 -I tools/build.py tools/data tools/template.html index.html https://escano-en-el-aire.pages.dev`
3. Comprobar que `index.html` contiene `og:image` con `https://escano-en-el-aire.pages.dev/og.jpg` y que carga.
4. Commit y push a `main`: Cloudflare Pages publica solo.

La web oculta las estimaciones sola desde el 24-nov-2026 a las 00:00 (hora de Madrid), por la veda de sondeos (art. 69.7 LOREG). No regenerar después del 23-nov.

## Modo veda (desde el 24-nov-2026 a las 00:00)
`python3 -I tools/build.py tools/data tools/template.html index.html https://escano-en-el-aire.pages.dev --veda`
Genera la web sin ningún dato de estimación en el código fuente (solo resultados de 2023). Ocultar con JavaScript no basta: los datos seguirían viéndose en el código de la página.
