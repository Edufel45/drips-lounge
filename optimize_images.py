"""Shrink product photos so the site loads fast.
Usage: python optimize_images.py "C:\\drips lounge products" "C:\\drips lounge products\\small"
"""
import sys
from pathlib import Path
from PIL import Image

src, dst = Path(sys.argv[1]), Path(sys.argv[2])
dst.mkdir(parents=True, exist_ok=True)
n = 0
for f in src.iterdir():
    if f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
        continue
    im = Image.open(f)
    im.thumbnail((900, 900))
    if im.mode != "RGB":
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[3])
        im = bg
    im.save(dst / (f.stem + ".webp"), quality=82, method=6)
    n += 1
print(n, "photos optimised ->", dst)
