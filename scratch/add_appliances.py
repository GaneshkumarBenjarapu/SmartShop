import json
import urllib.request
import os

def download(url, filepath):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        with open(filepath, 'wb') as f:
            f.write(response.read())

print("Downloading product images...")
download('https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?q=80&w=1000', 'frontend/static/philips_food_processor.png')
# download('https://images.unsplash.com/photo-1588854337236-6889d631faa8?q=80&w=1000', 'frontend/static/crompton_cooler.png') # Commented out: downloaded incorrect abstract art. Custom premium image generated.
# download('https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?q=80&w=1000', 'frontend/static/crompton_heater.png') # Commented out: downloaded incorrect living room photo. Custom premium image generated.
# download('https://images.unsplash.com/photo-1585515320310-259814833e62?q=80&w=1000', 'frontend/static/prestige_cooker.png') # Commented out: this was downloading a blender image instead of a rice cooker. We have generated a custom premium image.
print("Downloads completed.")

catalog_path = 'data/catalog.json'
with open(catalog_path, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Update existing brands
for p in catalog:
    if p.get('id') == 14:
        p['brand'] = 'philips'
    elif p.get('id') == 16:
        p['brand'] = 'prestige'

# Check if new products already exist (so we don't duplicate on re-run)
existing_ids = {p.get('id') for p in catalog}

new_products = [
    {
        "id": 9200,
        "name": "Philips Food Processor",
        "price": 8999,
        "description": "Multi-functional food processor with 30+ functions.",
        "category": "Home Appliances",
        "rating": 4.5,
        "image": "/static/philips_food_processor.png",
        "brand": "philips",
        "popularity": 1,
        "color": "black",
        "size": "standard",
        "discount": 10
    },
    {
        "id": 9201,
        "name": "Crompton Desert Air Cooler",
        "price": 11499,
        "description": "High-performance desert cooler with wood wool cooling pads.",
        "category": "Home Appliances",
        "rating": 4.4,
        "image": "/static/crompton_cooler.png",
        "brand": "crompton",
        "popularity": 1,
        "color": "white",
        "size": "75L",
        "discount": 15
    },
    {
        "id": 9202,
        "name": "Crompton Electric Water Heater",
        "price": 6299,
        "description": "5-star rated storage water heater with powerful heating.",
        "category": "Home Appliances",
        "rating": 4.3,
        "image": "/static/crompton_heater.png",
        "brand": "crompton",
        "popularity": 1,
        "color": "white",
        "size": "15L",
        "discount": 12
    },
    {
        "id": 9203,
        "name": "Prestige Electric Rice Cooker",
        "price": 2499,
        "description": "Automatic rice cooker with double-walled body.",
        "category": "Home Appliances",
        "rating": 4.4,
        "image": "/static/prestige_cooker.png",
        "brand": "prestige",
        "popularity": 1,
        "color": "red",
        "size": "1.8L",
        "discount": 8
    }
]

added_count = 0
for np in new_products:
    if np['id'] not in existing_ids:
        catalog.append(np)
        added_count += 1

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=4)

print(f"Added {added_count} new products to catalog.")
