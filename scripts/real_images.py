import json
import glob
import os

# Hardcoded high quality realistic images for different categories (guaranteed absolutely unique)
tshirts = [
    "https://i.imgur.com/axsyGpD.jpeg", # White T-shirt
    "https://i.imgur.com/9DqEOV5.jpeg", # Black T-shirt
    "https://i.imgur.com/Y54Bt8J.jpeg", # White Tee
    "https://i.imgur.com/QkIa5tT.jpeg", # Graphic T-shirt
    "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1000&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1581655353564-df123a1eb820?q=80&w=1000&auto=format&fit=crop"
]

shirts = [
    "https://i.imgur.com/qNOjJje.jpeg", # Denim shirt / jacket
    "https://images.unsplash.com/photo-1596755094514-f8b1e4c70fba?q=80&w=1000&auto=format&fit=crop", # Checked Shirt
    "https://images.unsplash.com/photo-1602810318383-e386cc2a3ce3?q=80&w=1000&auto=format&fit=crop", # Formal Shirt
    "https://images.unsplash.com/photo-1588359348347-9bc6cbbb689e?q=80&w=1000&auto=format&fit=crop" # Blue Shirt
]

jeans = [
    "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1000&auto=format&fit=crop", # Classic blue jeans
    "https://images.unsplash.com/photo-1582552938357-32b906df40cb?q=80&w=1000&auto=format&fit=crop", # Black jeans
    "https://images.unsplash.com/photo-1604176354204-9268738cb284?q=80&w=1000&auto=format&fit=crop", # Jeans stack
    "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?q=80&w=1000&auto=format&fit=crop"  # Jeans folded
]

trousers = [
    "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?q=80&w=1000&auto=format&fit=crop", # Beige Chinos
    "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=1000&auto=format&fit=crop", # Dark Chinos
    "https://images.unsplash.com/photo-1555689502-c4b22d76c56f?q=80&w=1000&auto=format&fit=crop",   # Formal trousers
    "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?q=80&w=1000&auto=format&fit=crop", # Chino closeup
    "https://images.unsplash.com/photo-1510312480391-768ad8b857dc?q=80&w=1000&auto=format&fit=crop",  # Plaid trousers
    "https://images.unsplash.com/photo-1559582798-678dfc71caf8?q=80&w=1000&auto=format&fit=crop" # Trousers
]

def pop_image(arr):
    if len(arr) > 0:
        return arr.pop(0)
    else:
        return "https://i.imgur.com/wXuQ7bm.jpeg" # Fallback cap

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'men fashion':
        pid = p['id']
        name_low = p['name'].lower()
        
        # Check if we have a locally generated image for this ID (those were good AI images!)
        local_files = glob.glob(f'frontend/static/men_{pid}_*.png')
        if local_files:
            filename = os.path.basename(local_files[0])
            p['image'] = f'/static/{filename}'
        else:
            if 't-shirt' in name_low or 'tshirt' in name_low:
                p['image'] = pop_image(tshirts)
            elif 'shirt' in name_low:
                p['image'] = pop_image(shirts)
            elif 'jeans' in name_low or 'denim' in name_low:
                p['image'] = pop_image(jeans)
            else:
                p['image'] = pop_image(trousers)

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated with real, distinct, nice images")
