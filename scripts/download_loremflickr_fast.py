import json, os, urllib.request
import concurrent.futures

d = 'frontend/static/generated'
os.makedirs(d, exist_ok=True)
c = 'data/catalog.json'

with open(c, 'r', encoding='utf-8') as f:
    data = json.load(f)

def download_image(p):
    cat = p.get('category', '').lower()
    if cat in ['men fashion', 'toys']:
        url = p.get('image', '')
        # Only rewrite if it's pollinations or doesn't exist locally
        if url.startswith('http') and 'pollinations.ai' in url:
            fname = f"generated_{p['id']}.jpg"
            fpath = os.path.join(d, fname)
            
            name = p.get('name', '').lower()
            keyword = 'fashion'
            if 'shirt' in name: keyword = 'tshirt'
            elif 'jean' in name or 'denim' in name: keyword = 'jeans'
            elif 'trouser' in name or 'chino' in name: keyword = 'trousers'
            elif 'suit' in name: keyword = 'suit'
            elif 'briefcase' in name: keyword = 'briefcase'
            
            if cat == 'toys':
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
                with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
                    f_out.write(res.read())
                p['image'] = f'/static/generated/{fname}'
                return True
            except Exception as e:
                print(f"Failed {p['id']}: {e}")
                return False
    return False

cnt = 0
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(download_image, data))
    cnt = sum(1 for r in results if r)

with open(c, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully downloaded and updated {cnt} images.")
