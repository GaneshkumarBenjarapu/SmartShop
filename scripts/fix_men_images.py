import json

def get_men_image(name):
    name_low = name.lower()
    if 't-shirt' in name_low or 'tshirt' in name_low:
        return 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1000&auto=format&fit=crop'
    elif 'shirt' in name_low:
        return 'https://images.unsplash.com/photo-1596755094514-f8b1e4c70fba?q=80&w=1000&auto=format&fit=crop'
    elif 'jeans' in name_low or 'denim' in name_low:
        return 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1000&auto=format&fit=crop'
    elif 'trouser' in name_low or 'chino' in name_low:
        return 'https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?q=80&w=1000&auto=format&fit=crop'
    else:
        return 'https://images.unsplash.com/photo-1490578474895-699bc4e35154?q=80&w=1000&auto=format&fit=crop'

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for p in data:
    if p.get('category', '').lower() == 'men fashion':
        old = p['image']
        new_img = get_men_image(p.get('name', ''))
        if old != new_img:
            p['image'] = new_img
            count += 1

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Updated {count} products in data/catalog.json")
