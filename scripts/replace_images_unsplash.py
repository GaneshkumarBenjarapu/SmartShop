import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'

category_map = {
    'Electronics': 'electronics gadget',
    'Home Appliances': 'home appliance kitchen',
    'Beauty': 'beauty perfume',
    'Books': 'books reading',
    'Shoes': 'shoes sneakers',
    'Men Fashion': 'men fashion clothing',
    'Women Fashion': 'women fashion clothing',
    'Kidsware': 'kids toys',
    'Toys': 'toys children',
    'Home & Kitchen': 'home kitchen'
}

with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = 0
for p in data:
    cid = p.get('id', 0)
    cat = p.get('category', '')
    # choose query
    query = category_map.get(cat, '')
    if not query:
        # fallback to sanitized product name words
        name = p.get('name', '')
        query = ' '.join(name.split()[:3]) or 'product'
    # use source.unsplash.com with sig to vary images per id
    url = f"https://source.unsplash.com/1000x1000/?{query}&sig={cid}"
    p['image'] = url
    updated += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated {updated} products' image URLs in {CATALOG}")
