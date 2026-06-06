import json
import glob
import os

def get_keyword(name):
    name_low = name.lower()
    if 't-shirt' in name_low or 'tshirt' in name_low:
        return 'tshirt,mens'
    elif 'shirt' in name_low:
        return 'shirt,mens'
    elif 'jeans' in name_low or 'denim' in name_low:
        return 'jeans,mens'
    elif 'trouser' in name_low or 'chino' in name_low:
        return 'trousers,mens'
    else:
        return 'mens,fashion'

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'men fashion':
        pid = p['id']
        
        # Check if we have a locally generated image for this ID
        local_files = glob.glob(f'frontend/static/men_{pid}_*.png')
        if local_files:
            filename = os.path.basename(local_files[0])
            p['image'] = f'/static/{filename}'
        else:
            # Use loremflickr to guarantee unique relevant image
            kw = get_keyword(p['name'])
            p['image'] = f'https://loremflickr.com/800/1000/{kw}/all?lock={pid}'

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated catalog.json with 100% unique images")
