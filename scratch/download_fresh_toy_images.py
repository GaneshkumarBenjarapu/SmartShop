import os, json, urllib.request, urllib.parse, time

catalog_path = 'data/catalog.json'
static_dir = 'frontend/static/toys_fresh'
os.makedirs(static_dir, exist_ok=True)

with open(catalog_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for product in data:
    if product.get('category') == 'Toys':
        pid = product['id']
        name = product['name']
        # Build a simple keyword query from name
        query = urllib.parse.quote(name)
        # Use Unsplash source (random image for query)
        url = f'https://source.unsplash.com/1000x1000/?{query}'
        fname = f'toy_{pid}_fresh.jpg'
        fpath = os.path.join(static_dir, fname)
        try:
            print(f'Downloading image for {name} from Unsplash...')
            req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=20) as res, open(fpath, 'wb') as out:
                out.write(res.read())
            product['image'] = f'/static/toys_fresh/{fname}'
        except Exception as e:
            print(f'Failed to download {name}:', e)
        time.sleep(1)  # be gentle to the service

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
print('Catalog updated with fresh Unsplash images.')
