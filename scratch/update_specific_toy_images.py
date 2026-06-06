import os, json, urllib.request, urllib.parse, time

CATALOG_PATH = 'data/catalog.json'
STATIC_DIR = 'frontend/static/toys_fresh'
os.makedirs(STATIC_DIR, exist_ok=True)

# Target product names (exact as they appear in catalog)
TARGET_NAMES = [
    'Creative Arts & Crafts Slime Kit',
    'Musical Learning Toy Mobile',
    'Classic Ceramic Piggy Money Bank',
    'Wooden Chess & Board Game Set'
]

# Load catalog
with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

updated = 0
for product in data:
    if product.get('category') != 'Toys':
        continue
    name = product.get('name')
    if name not in TARGET_NAMES:
        continue
    pid = product.get('id')
    # Build Unsplash query from name (remove special chars)
    query = urllib.parse.quote(name)
    url = f'https://source.unsplash.com/1000x1000/?{query}'
    fname = f'toy_{pid}_fresh.jpg'
    fpath = os.path.join(STATIC_DIR, fname)
    try:
        print(f'Downloading image for "{name}" (id {pid}) from {url}...')
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=20) as resp, open(fpath, 'wb') as out:
            out.write(resp.read())
        # Update catalog path
        product['image'] = f'/static/toys_fresh/{fname}'
        updated += 1
    except Exception as e:
        print(f'Failed to download image for {name}: {e}')
    time.sleep(1)  # be gentle to the service

# Write back catalog
with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f'Updated images for {updated} products.')
