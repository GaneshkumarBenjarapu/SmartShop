import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'catalog.json'

# simple stopwords to drop from queries
stop = set(["the","and","with","for","a","an","of","in","on","to","by","&"])

def slugify_query(text):
    # keep alphanumerics and spaces
    txt = re.sub(r"[^A-Za-z0-9 ]+", ' ', text)
    words = [w for w in txt.split() if w and w.lower() not in stop]
    # take first meaningful words (limit 4)
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

with open(CATALOG, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = 0
for p in data:
    pid = p.get('id')
    name = p.get('name','')
    cat = p.get('category','')
    base = slugify_query(name) or slugify_query(p.get('description','')) or cat
    boost = category_boost.get(cat, '')
    query = f"{base} {boost}" if boost else base
    # replace spaces with commas for Unsplash to match multiple keywords
    query_param = ','.join(query.split())
    p['image'] = f"https://source.unsplash.com/1000x1000/?{query_param}&sig={pid}"
    # also set images array if not present to provide gallery fallback
    if not p.get('images'):
        p['images'] = [p['image']]
    updated += 1

with open(CATALOG, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"Updated {updated} products in {CATALOG}")
