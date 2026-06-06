import json
import urllib.request
import os

images = {
    'board game': [
        'https://images.unsplash.com/photo-1611883398939-509a25bdf255?q=80&w=1000&auto=format&fit=crop',
        'https://images.unsplash.com/photo-1594498653371-3c58b4ef2136?q=80&w=1000&auto=format&fit=crop'
    ],
    'action figure': [
        'https://images.unsplash.com/photo-1608889175250-c3b0c1667d3a?q=80&w=1000&auto=format&fit=crop',
        'https://images.unsplash.com/photo-1590622956272-a169b00debed?q=80&w=1000&auto=format&fit=crop'
    ],
    'puzzle': [
        'https://images.unsplash.com/photo-1585847321591-6de1762c4731?q=80&w=1000&auto=format&fit=crop',
        'https://images.unsplash.com/photo-1629853900223-289b53e8d249?q=80&w=1000&auto=format&fit=crop'
    ]
}
pointers = {'board game': 0, 'action figure': 0, 'puzzle': 0}

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        pid = p['id']
        path = f'frontend/static/toy_real_{pid}.jpg'
        
        # Determine if it's missing or an empty file
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            name_low = p['name'].lower()
            cat = 'puzzle'
            if 'board game' in name_low: cat = 'board game'
            elif 'action figure' in name_low: cat = 'action figure'
            
            arr = images[cat]
            img_url = arr[pointers[cat] % len(arr)]
            pointers[cat] += 1
            
            print(f"Fixing missing toy {pid}: {p['name']} -> {img_url}")
            try:
                req = urllib.request.Request(img_url, headers={'User-Agent': f'CoolShopBot_{pid}/1.0'})
                with urllib.request.urlopen(req, timeout=30) as response, open(path, 'wb') as out_file:
                    out_file.write(response.read())
                
                print("Success")
            except Exception as e:
                print(f"Failed again on {img_url}: {e}")

print("Done un-breaking toys.")
