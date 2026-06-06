import json
import urllib.request
import os
import time

amazon_toys = [
    {"asin": "B00000IZSI", "name": "UNO Family Card Game"},
    {"asin": "B00NHQFA1I", "name": "LEGO Classic Large Creative Brick Box"},
    {"asin": "B00ABA0ZOA", "name": "Jenga Classic Game"},
    {"asin": "B00D8STBHY", "name": "Hasbro Connect 4 Game"},
    {"asin": "B00000IWDO", "name": "Operation Classic Board Game"},
    {"asin": "B00D8TOEIW", "name": "Hasbro Guess Who? Game"},
    {"asin": "B00D4NFSFE", "name": "Trouble Board Game"},
    {"asin": "B00JM5GW10", "name": "Play-Doh Modeling Compound 10-Pack Case"},
    {"asin": "B004HFPV12", "name": "Rubik's Cube 3x3 Puzzle Game"},
    {"asin": "B00C0XBIZW", "name": "Battleship Classic Board Game"},
    {"asin": "B008D6N7G0", "name": "Twister Ultimate Game"},
    {"asin": "B01LYX0I8P", "name": "Nerf N-Strike Elite Disruptor Blaster"},
    {"asin": "B0007R4KQ8", "name": "Hot Wheels 9-Car Gift Pack"},
    {"asin": "B004S8F7QM", "name": "Cards Against Humanity"},
    {"asin": "B00U26V4VQ", "name": "CATAN Board Game (Base Game)"}
]

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

toy_index = 0
for p in data:
    if p.get('category', '').lower() == 'toys':
        if toy_index < len(amazon_toys):
            toy_data = amazon_toys[toy_index]
            asin = toy_data["asin"]
            toy_name = toy_data["name"]
            
            p['name'] = toy_name
            
            img_url = f'https://images-na.ssl-images-amazon.com/images/P/{asin}.01.LZZZZZZZ.jpg'
            local_name = f'amazon_toy_{asin}.jpg'
            local_path = os.path.join('frontend', 'static', local_name)
            
            print(f"Downloading {toy_name}...")
            
            try:
                time.sleep(0.5)
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as response, open(local_path, 'wb') as out_file:
                    out_file.write(response.read())
                
                # Check if Amazon actually returned a valid image (sometimes it returns a 1x1 GIF)
                if os.path.getsize(local_path) > 100:
                    p['image'] = f"/static/{local_name}"
                else:
                    p['image'] = img_url # fallback
                    
            except Exception as e:
                print(f"Failed on {img_url}: {e}")
                
            toy_index += 1

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Successfully replaced {toy_index} toys with Amazon products!")
