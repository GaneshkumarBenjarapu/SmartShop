import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'

with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

modified = 0
for p in data:
    if p.get('category') == 'Books':
        name = p.get('name','').lower()
        base_img = p.get('image')
        # ensure base image exists
        if not base_img:
            base_img = f"https://source.unsplash.com/1000x1000/?books&sig={p.get('id')}"
            p['image'] = base_img
        if 'self-help' in name or 'self help' in name or 'self-help guide' in name:
            # ensure single images array with base_img
            p['images'] = [base_img]
            modified += 1
        elif 'biography' in name or 'biography' in p.get('description','').lower():
            # ensure two images: base_img and a secondary variant
            sec = base_img
            if 'images.unsplash.com' in base_img:
                sec = base_img.replace('q=80', 'q=80&w=1000&auto=format&fit=crop')
            else:
                sec = f"https://source.unsplash.com/1000x1000/?biography&sig={p.get('id')+500}"
            p['images'] = [base_img, sec]
            modified += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated images for {modified} book products in {CATALOG}")
