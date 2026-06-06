import json
import urllib.request
import os

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, p in enumerate(data):
    if p.get('category', '').lower() == 'men fashion':
        img = p.get('image', '')
        if img.startswith('http'):
            pid = p['id']
            ext = 'jpg'
            if '.png' in img: ext = 'png'
            elif '.jpeg' in img: ext = 'jpeg'
            
            local_name = f"men_real_{pid}.{ext}"
            local_path = os.path.join('frontend', 'static', local_name)
            
            try:
                print(f"Downloading {img} to {local_name}...")
                req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
                
                # Update catalog
                p['image'] = f"/static/{local_name}"
            except Exception as e:
                print(f"Failed to download {img}: {e}")
                
with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Finished downloading images locally.")
