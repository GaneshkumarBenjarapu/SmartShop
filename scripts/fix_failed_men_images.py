import json
import urllib.request
import os

fix_map = {
    62: ("Casual Shirt", "https://image.pollinations.ai/prompt/professional%20mens%20casual%20shirt%20product%20photography%20white%20background?width=800&height=1000&nologo=true&seed=62"),
    145: ("Formal Shirt", "https://image.pollinations.ai/prompt/professional%20mens%20formal%20white%20shirt%20product%20photography%20white%20background?width=800&height=1000&nologo=true&seed=145"),
    146: ("Regular Fit Jeans", "https://image.pollinations.ai/prompt/professional%20mens%20blue%20jeans%20product%20photography%20white%20background?width=800&height=1000&nologo=true&seed=146"),
    151: ("Cargo Trousers", "https://image.pollinations.ai/prompt/professional%20mens%20cargo%20trousers%20pants%20product%20photography%20white%20background?width=800&height=1000&nologo=true&seed=151"),
    156: ("Slim Fit Chino Trousers", "https://image.pollinations.ai/prompt/professional%20mens%20slim%20fit%20chino%20trousers%20product%20photography%20white%20background?width=800&height=1000&nologo=true&seed=156"),
}

def fix_failed_images():
    os.makedirs('frontend/static/men_unique', exist_ok=True)
    
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('category', '').lower() == 'men fashion' and p.get('id') in fix_map:
            name, url = fix_map[p['id']]
            filename = f"men_unique_{p['id']}.jpg"
            filepath = os.path.join('frontend', 'static', 'men_unique', filename)
            
            print(f"Downloading {filename} for {name}...")
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

    print("Finished fixing missing images.")

if __name__ == '__main__':
    fix_failed_images()
