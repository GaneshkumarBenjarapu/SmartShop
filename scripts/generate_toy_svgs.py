import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'
OUTDIR = ROOT / 'static' / 'toys'
OUTDIR.mkdir(parents=True, exist_ok=True)

emoji_map = [
    '🧸','🚗','🪀','🧩','🪁','🎲','👾','🪄','🤖','🐻'
]

with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = 0
for p in data:
    if p.get('category','').lower() == 'toys':
        pid = p.get('id')
        name = p.get('name','Toy')
        # pick an emoji deterministically per id
        emoji = emoji_map[pid % len(emoji_map)]
        # choose random palette seeded by id for consistency
        random.seed(pid)
        bg1 = "#{:06x}".format(random.randint(0xA0A0A0, 0xFFF0F0))
        bg2 = "#{:06x}".format(random.randint(0xA0A0A0, 0xFFF0F0))
        text_color = '#111827'
        filename = f"toy_{pid}.svg"
        filepath = OUTDIR / filename
        svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000" viewBox="0 0 1000 1000">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{bg1}" />
      <stop offset="100%" stop-color="{bg2}" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#g)" />
  <g transform="translate(0,0)">
    <text x="50%" y="46%" font-size="320" text-anchor="middle" dominant-baseline="middle">{emoji}</text>
    <text x="50%" y="78%" font-size="44" text-anchor="middle" fill="{text_color}" font-family="Arial, Helvetica, sans-serif">{name}</text>
  </g>
</svg>
'''
        with open(filepath, 'w', encoding='utf-8') as out:
            out.write(svg)
        p['image'] = f"/static/toys/{filename}"
        updated += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Generated {updated} toy SVGs into {OUTDIR}")
