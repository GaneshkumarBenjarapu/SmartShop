import json
import urllib.request
import os
import time

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        pid = p['id']
        path = f'frontend/static/toy_real_{pid}.jpg'
        
        # If still missing or empty
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            name_low = p['name'].lower()
            keyword = 'puzzle,jigsaw'
            if 'block' in name_low: keyword = 'lego,blocks'
            elif 'action figure' in name_low: keyword = 'actionfigure,toy'
            
            # Use loremflickr to get a perfect unique image based on keyword + lock
            img_url = f'https://loremflickr.com/800/1000/{keyword}/all?lock={pid}'
            print(f"Fixing finally {pid} with {keyword}...")
            
            try:
                # loremflickr responds well, no 429 normally
                time.sleep(1)
                req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as response, open(path, 'wb') as out_file:
                    out_file.write(response.read())
                
                print("Success")
            except Exception as e:
                print(f"Failed on {img_url}: {e}")

print("Final patch complete.")
