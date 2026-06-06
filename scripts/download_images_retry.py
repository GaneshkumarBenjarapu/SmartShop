import json, os, urllib.request, time

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
        # Check if it was already successfully downloaded
        if url and url.startswith('http') and 'pollinations.ai' in url:
            fname = f"generated_{p['id']}.jpg"
            fpath = os.path.join(d, fname)
            print(f"Downloading for {p['id']} - {p['name']}...")
            
            success = False
            for attempt in range(5):
                try:
                    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=30) as res, open(fpath, 'wb') as f_out:
                        f_out.write(res.read())
                    p['image'] = f'/static/generated/{fname}'
                    cnt += 1
                    success = True
                    print(f"  Success!")
                    time.sleep(1) # wait between success too
                    break
                except Exception as e:
                    print(f"  Failed attempt {attempt+1}: {e}")
                    time.sleep(2 * (attempt + 1)) # exponential backoff
            
            if not success:
                # Fallback to loremflickr using the first word or main noun of the name
                print(f"  Falling back to loremflickr...")
                name = p['name'].lower()
                keyword = 'fashion'
                if 'shirt' in name: keyword = 'tshirt'
                elif 'jean' in name or 'denim' in name: keyword = 'jeans'
                elif 'trouser' in name or 'chino' in name: keyword = 'trousers'
                elif 'suit' in name: keyword = 'suit'
                elif 'briefcase' in name: keyword = 'briefcase'
                
                # Toys keywords
                if 'lego' in name or 'brick' in name: keyword = 'lego'
                elif 'game' in name: keyword = 'boardgame'
                elif 'puzzle' in name or 'rubik' in name: keyword = 'rubikscube'
                elif 'blaster' in name or 'nerf' in name: keyword = 'toygun'
                elif 'car' in name: keyword = 'toycar'
                elif 'play-doh' in name: keyword = 'playdoh'
                elif 'uno' in name or 'cards' in name: keyword = 'cardgame'
                
                fb_url = f'https://loremflickr.com/800/1000/{keyword}/all?lock={p["id"]}'
                try:
                    req = urllib.request.Request(fb_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req, timeout=30) as res, open(fpath, 'wb') as f_out:
                        f_out.write(res.read())
                    p['image'] = f'/static/generated/{fname}'
                    cnt += 1
                    print(f"  Success with fallback!")
                except Exception as e:
                    print(f"  Complete failure for {p['id']}: {e}")

with open(c, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully downloaded and updated {cnt} images.")
