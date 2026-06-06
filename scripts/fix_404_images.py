import json
import urllib.request
import os

fallbacks = [
    "https://i.imgur.com/T8oq9X2.jpeg",
    "https://i.imgur.com/qNOjJje.jpeg",
    "https://i.imgur.com/ZANVnHE.jpeg"
]

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, p in enumerate(data):
    if p['id'] in [151, 154, 156]:
        img = fallbacks.pop(0)
        local_name = f"men_real_{p['id']}.jpeg"
        local_path = os.path.join('frontend', 'static', local_name)
        
        try:
            print(f"Downloading {img} to {local_name}...")
            req = urllib.request.Request(img, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
            
            p['image'] = f"/static/{local_name}"
        except Exception as e:
            print(f"Failed to download {img}: {e}")

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Fixed the 404 images.")
