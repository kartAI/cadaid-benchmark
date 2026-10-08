# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow"]
# ///
"""Render annotated sample images (docs/samples/*.png) for the README preview grid."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "samples"
MAX_SIDE = 1000
COLORS = {0: (230, 57, 70), 1: (29, 120, 220), 2: (40, 167, 69), 3: (255, 159, 28)}

SAMPLES = [
    "Reinsdyrveien20_fasade_page_3.jpg",
    "Soleieveien 44_plantegning1_page_1.jpg",
    "Stoltangen1_situasjonskart_page_1.jpg",
    "Skippergata_snitt_page_1.jpg",
    "Harebakkveien38_plan_fasade_snitt_page_1.jpg",
    "Brunsbykollen9_fasade_page_1.jpg",
    "Grovene30_plan_snitt_page_1.jpg",
    "Tegning E-5.pdf_page_1.jpg",
    "Buggelandsbakken156_alle_tegninger_page_1.jpg",
]


def font(size):
    for f in ("/System/Library/Fonts/Helvetica.ttc", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(f, size)
        except OSError:
            pass
    return ImageFont.load_default()


def main():
    records = {r["image"]: r for r in json.loads((ROOT / "data/labels.json").read_text())}
    OUT.mkdir(parents=True, exist_ok=True)
    for i, name in enumerate(SAMPLES, 1):
        rec = records[name]
        img = Image.open(ROOT / "data/images" / name).convert("RGB")
        s = MAX_SIDE / max(img.size)
        img = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
        d = ImageDraw.Draw(img)
        f = font(max(16, MAX_SIDE // 45))
        for l in rec["labels"]:
            c = COLORS[l["label"]]
            x0, y0, x1, y1 = (v * s for v in l["bbox"])
            d.rectangle((x0, y0, x1, y1), outline=c, width=4)
            tag = f"{l['label']} {l['text']}"
            tb = d.textbbox((x0, y0), tag, font=f)
            d.rectangle((tb[0], tb[1] - 4, tb[2] + 8, tb[3] + 4), fill=c)
            d.text((x0 + 4, y0), tag, fill="white", font=f)
        if not rec["labels"]:
            d.text((12, 8), "no labels", fill=(120, 120, 120), font=f)
        img.save(OUT / f"sample_{i}.png", optimize=True)
        print(i, name, [l["text"] for l in rec["labels"]])


main()
