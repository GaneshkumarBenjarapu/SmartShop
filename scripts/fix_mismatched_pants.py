import urllib.request
import re
import json

def get_image(query):
    req = urllib.request.Request(f'https://unsplash.com/s/photos/{query}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        urls = re.findall(r'(https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+)', html)
        if urls:
            return list(set(urls))
    except Exception as e:
        print(e)
    return []

# Use multiple fallbacks
jeans_urls = get_image('mens-blue-jeans') or [
    "https://images.unsplash.com/photo-1582552938357-32b906df40cb"
]

trousers_urls = get_image('formal-mens-trousers') or [
    "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80",
    "https://images.unsplash.com/photo-1594938298603-c8148c4dae35"
]

url_jeans = jeans_urls[0] + "?q=80&w=1000&auto=format&fit=crop"
url_trousers1 = trousers_urls[0] + "?q=80&w=1000&auto=format&fit=crop"
url_trousers2 = trousers_urls[1] + "?q=80&w=1000&auto=format&fit=crop"

to_fix = {
    154: url_jeans,
    151: url_trousers1,
    156: url_trousers2
}

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p['id'] in to_fix:
        img_url = to_fix[p['id']]
        local_name = f"men_real_{p['id']}.jpg"
        local_path = f"frontend/static/{local_name}"
        
        try:
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as response, open(local_path, 'wb') as out:
                out.write(response.read())
            p['image'] = f"/static/{local_name}"
            print(f"Fixed {p['id']} - {p['name']} with {p['image']}")
        except Exception as e:
            print(f"Error on {p['id']}: {e}")

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Fix completed.")
