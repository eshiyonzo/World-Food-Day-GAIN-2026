#!/usr/bin/env bash
# Rebuilds the A2 CMYK print files from the HTML sources.
# Needs: node + playwright (Chromium), python3 with pypdf, pikepdf, numpy, and ghostscript (gs).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p out

# 1. HTML -> RGB PDF at A3 (artwork is designed on a 420 x 297 mm canvas)
node render.js frame placard
( cd qr && node -e "
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.cwd()+'/stickers.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:'stickers.pdf',width:'210mm',height:'297mm',printBackground:true,margin:{top:0,right:0,bottom:0,left:0}});await b.close();})()" )

# 2. Split placard into red / white pages
python3 - <<'EOF'
from pypdf import PdfReader, PdfWriter
r = PdfReader('placard.pdf')
for i, n in enumerate(['placard_red', 'placard_white']):
    w = PdfWriter(); w.add_page(r.pages[i]); w.write(f'out/{n}_rgb.pdf')
EOF
cp frame.pdf out/frame_rgb.pdf

# 3. RGB -> CMYK with exact GAIN brand values
for f in frame placard_red placard_white; do
  python3 ../tools/to_cmyk.py out/${f}_rgb.pdf out/${f}_cmyk_A3.pdf
done
python3 ../tools/to_cmyk.py qr/stickers.pdf out/GAIN_WFD2026_QR_Stickers_A4.pdf

# 4. Scale A3 -> A2 (vector, no quality loss)
python3 - <<'EOF'
from pypdf import PdfReader, PdfWriter
s = 594 / 420
for src, dst in [('frame', 'GAIN_WFD2026_Photo_Frame_A2_CMYK'),
                 ('placard_red', 'GAIN_WFD2026_Placard_Red_A2_CMYK'),
                 ('placard_white', 'GAIN_WFD2026_Placard_White_A2_CMYK')]:
    r = PdfReader(f'out/{src}_cmyk_A3.pdf'); w = PdfWriter()
    p = r.pages[0]; p.scale_by(s); w.add_page(p); w.write(f'out/{dst}.pdf')
EOF
echo "Done. Final files are in design/out/"
# Note: in the QR sticker PDF, the QR pixels were additionally forced to 100% K
# (see HANDOVER.md, 'QR code'). Re-apply that step if you rebuild the stickers.
