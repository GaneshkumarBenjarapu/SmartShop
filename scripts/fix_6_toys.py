import json
import urllib.request
import os

fixes = {
    "B0007R4KQ8": "https://images.unsplash.com/photo-1581235720704-06d3acfcb36f?q=80&w=1000&auto=format&fit=crop", # Hot wheels
    "B004HFPV12": "https://images.unsplash.com/photo-1591991731833-b4807cf7ef94?q=80&w=1000&auto=format&fit=crop", # Rubiks cube
    "B008D6N7G0": "https://images.unsplash.com/photo-1587654780291-39c9404d746b?q=80&w=1000&auto=format&fit=crop", # Twister
    "B00C0XBIZW": "https://loremflickr.com/800/1000/boardgame/all?lock=500", # Battleship
    "B00D4NFSFE": "https://loremflickr.com/800/1000/boardgame/all?lock=501", # Trouble
    "B00D8TOEIW": "https://loremflickr.com/800/1000/boardgame/all?lock=502"  # Guess who
}

for asin, img_url in fixes.items():
    local_name = f'amazon_toy_{asin}.jpg'
    local_path = os.path.join('frontend', 'static', local_name)
    print(f"Downloading {asin}...")
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded {asin}")
    except Exception as e:
        print(f"Failed {asin}: {e}")

# Trigger DB sync by touching catalog.json
import sqlite3
conn = sqlite3.connect('data/shop.db')
c = conn.cursor()
with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        if 'amazon_toy' in p.get('image', ''):
            pass # Keep it, the file on disk was overwritten so python will serve it automatically
            # Let's ensure the path in DB is correct:
            c.execute('UPDATE products SET image = ? WHERE id = ?', (p.get('image', ''), p['id']))

conn.commit()
conn.close()

# touch json
with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Fixed broken toys.")
