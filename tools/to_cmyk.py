import sys, re, subprocess, numpy as np, pikepdf, zlib
src, out = sys.argv[1], sys.argv[2]
tmp = out + '.gs.pdf'
subprocess.run(['gs','-q','-dSAFER','-dBATCH','-dNOPAUSE','-sDEVICE=pdfwrite',
  '-sColorConversionStrategy=CMYK','-sProcessColorModel=DeviceCMYK','-dOverrideICC',
  '-dPDFSETTINGS=/prepress','-o',tmp,src],check=True)
# converted value -> GAIN brand CMYK (from GAIN Brand Identity Guidelines)
MAP = {
 (0.271,1,0.69,0.216): '0 0.78 0.31 0.43',    # GAIN Red #98103A
 (0.008,0.122,0.996,0): '0 0.15 0.95 0',      # Yellow #FFD80D
 (0.69,0.655,0.678,0.769): '0.5 0.4 0.4 1',   # GAIN Black #1D1D1B
 (0.722,0.675,0.671,0.882): '0 0 0 1',        # trim marks: pure black
 (0.271,0.227,0.231,0): '0 0 0 0.37',         # Grey #B9B8B8
 (0.537,0.463,0.463,0.11): '0 0 0 0.6',       # small print grey
 (0.471,0.4,0.404,0.039): '0 0 0 0.55',       # hint grey
}
num = r'(\d*\.?\d+)'
pat = re.compile((num+r'\s+')*4 + r'(k|K)\b')
def fix(data):
    s = data.decode('latin-1'); hits=[0]
    def rep(m):
        v = tuple(float(x) for x in m.groups()[:4])
        for k, b in MAP.items():
            if all(abs(a-c) < 0.003 for a, c in zip(v, k)):
                hits[0]+=1; return f'{b} {m.group(5)}'
        return m.group(0)
    return pat.sub(rep, s).encode('latin-1'), hits[0]
pdf = pikepdf.open(tmp)
total=0
for obj in pdf.objects:
    if isinstance(obj, pikepdf.Stream) and obj.get('/Subtype') != '/Image':
        try: data = obj.read_bytes()
        except Exception: continue
        new, n = fix(data)
        if n: obj.write(new); total+=n
# raster logo: snap near-red pixels to brand red
red_conv = np.array([0.271,1,0.69,0.216])*255; red_brand=np.array([0,0.78,0.31,0.43])*255
for obj in pdf.objects:
    if isinstance(obj, pikepdf.Stream) and obj.get('/Subtype')=='/Image' and obj.get('/ColorSpace')=='/DeviceCMYK':
        w,h=int(obj.Width),int(obj.Height)
        a=np.frombuffer(obj.read_bytes(),dtype=np.uint8).reshape(h,w,4).astype(float)
        d=np.abs(a-red_conv).max(axis=2)
        mask=d<40
        if mask.any():
            a[mask]=red_brand; total+=int(mask.sum()>0)
            obj.write(zlib.compress(a.round().astype(np.uint8).tobytes()), filter=pikepdf.Name.FlateDecode)
pdf.save(out); pdf.close()
import os; os.remove(tmp)
print(out, 'colour fixes:', total)
