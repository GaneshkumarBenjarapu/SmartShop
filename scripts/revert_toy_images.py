import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'
TOY_DIR = ROOT / 'static' / 'toys'

with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

reverted = 0
for p in data:
    img = p.get('image','')
    if isinstance(img, str) and img.startswith('/static/toys/'):
        pid = p.get('id', 0)
        p['image'] = f"https://source.unsplash.com/1000x1000/?kids toys&sig={pid}"
        reverted += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# remove generated toy svgs
removed = 0
if TOY_DIR.exists():
    for p in TOY_DIR.glob('toy_*.svg'):
        try:
            p.unlink()
            removed += 1
        except Exception:
            pass

print(f"Reverted {reverted} catalog entries and removed {removed} files from {TOY_DIR}")
