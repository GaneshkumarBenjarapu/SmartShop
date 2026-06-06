import json, os, urllib.request

d = 'frontend/static/generated'
os.makedirs(d, exist_ok=True)
c = 'data/catalog.json'

with open(c, 'r', encoding='utf-8') as f:
    data = json.load(f)

cnt = 0
for p in data:
    cat = p.get('category', '').lower()
    if cat in ['men fashion', 'toys']:
        url = p.get('image')
        if url and url.startswith('http'):
            fname = f"generated_{p['id']}.jpg"
            fpath = os.path.join(d, fname)
            print(f"Downloading for {p['id']}...")
            try:
                # Add headers to avoid some basic blocks
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
                    f_out.write(res.read())
                
                # Update the URL to local path
                # Browsers accessing /static map it here
                p['image'] = f'/static/generated/{fname}'
                cnt += 1
            except Exception as e:
                print(f"Failed {p['id']}: {e}")

with open(c, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully downloaded and updated {cnt} images.")
