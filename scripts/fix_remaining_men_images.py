import json
import urllib.request
import os

fix_map = {
    145: ("Formal Shirt", "https://loremflickr.com/800/1000/mens,formal,shirt/all?lock=145"),
    146: ("Regular Fit Jeans", "https://loremflickr.com/800/1000/mens,jeans/all?lock=146"),
    151: ("Cargo Trousers", "https://loremflickr.com/800/1000/mens,pants/all?lock=151"),
    156: ("Slim Fit Chino Trousers", "https://loremflickr.com/800/1000/mens,trousers/all?lock=156"),
}

def fix_remaining_images():
    os.makedirs('frontend/static/men_unique', exist_ok=True)
    
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('category', '').lower() == 'men fashion' and p.get('id') in fix_map:
            name, url = fix_map[p['id']]
            filename = f"men_unique_{p['id']}.jpg"
            filepath = os.path.join('frontend', 'static', 'men_unique', filename)
            
            print(f"Downloading {filename} for {name} from LoremFlickr...")
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as res, open(filepath, 'wb') as f_out:
                    f_out.write(res.read())
                
                # Update the URL to local path
                p['image'] = f'/static/men_unique/{filename}'
            except Exception as e:
                print(f"Failed {p['id']}: {e}")

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print("Finished fixing remaining missing images.")

if __name__ == '__main__':
    fix_remaining_images()
