import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'
STATIC = ROOT / 'static'

# helper to slugify
stop = set(["the","and","with","for","a","an","of","in","on","to","by","&"])
def slugify_query(text):
    txt = re.sub(r"[^A-Za-z0-9 ]+", ' ', text)
    words = [w for w in txt.split() if w and w.lower() not in stop]
    return ' '.join(words[:4])

category_boost = {
    'Electronics': 'electronics product studio',
    'Home Appliances': 'appliance product studio',
    'Beauty': 'beauty product studio white background',
    'Books': 'book cover photography',
    'Shoes': 'shoe product photography',
    'Men Fashion': 'mens clothing product',
    'Women Fashion': 'womens clothing product',
    'Kidsware': 'kids clothing toy product',
    'Toys': 'toy product photography',
}

# Load catalog
with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

generated = 0
updated = 0
missing_files = set()

for p in data:
    pid = p.get('id')
    name = p.get('name','')
    cat = p.get('category','')
    # collect static references from image or images
    static_paths = []
    if isinstance(p.get('image',''), str) and p['image'].startswith('/static/'):
        static_paths.append(p['image'])
    if isinstance(p.get('images', None), list):
        for img in p['images']:
            if isinstance(img, str) and img.startswith('/static/') and img not in static_paths:
                static_paths.append(img)

    # ensure static files exist by creating SVG placeholders
    for sp in static_paths:
        spath = (ROOT / sp.lstrip('/'))
        if not spath.exists():
            spath.parent.mkdir(parents=True, exist_ok=True)
            # generate simple SVG with product name and id
            random.seed(pid)
            bg = "#{:06x}".format(random.randint(0xA0A0A0, 0xFFFFFF))
            fg = '#111827'
            title = (name[:30] + '...') if len(name) > 30 else name
            svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1000" viewBox="0 0 1000 1000">
  <rect width="100%" height="100%" fill="{bg}" />
  <text x="50%" y="50%" font-size="32" text-anchor="middle" fill="{fg}" font-family="Arial, Helvetica, sans-serif">{title}</text>
  <text x="50%" y="60%" font-size="20" text-anchor="middle" fill="{fg}" font-family="Arial, Helvetica, sans-serif">ID: {pid}</text>
</svg>
'''
            with open(spath, 'w', encoding='utf-8') as out:
                out.write(svg)
            generated += 1
        else:
            # file exists
            pass

    # build Unsplash amazon-style URL
    base = slugify_query(name) or slugify_query(p.get('description','')) or cat
    boost = category_boost.get(cat, '')
    query = f"{base} {boost}" if boost else base
    query_param = ','.join(query.split())
    unsplash = f"https://source.unsplash.com/1000x1000/?{query_param}&sig={pid}"

    # ensure images array: unsplash first, then any existing static paths
    new_images = [unsplash]
    for sp in static_paths:
        # convert to absolute path prefixed with /static/
        new_images.append(sp)
    p['image'] = unsplash
    p['images'] = new_images
    updated += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Generated {generated} static placeholder files; updated {updated} products in {CATALOG}")
