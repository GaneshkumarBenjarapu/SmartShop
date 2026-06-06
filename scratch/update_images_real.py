import json
import os
import requests
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]
CATALOG_PATH = r"c:/Users/DELL/OneDrive/Desktop/Product recommendation/data/catalog.json"
STATIC_IMG_DIR = BASE_DIR / 'frontend' / 'static' / 'toys_final'
STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)

# Target product names
TARGET_NAMES = [
    "Creative Arts & Crafts Slime Kit",
    "Musical Learning Toy Mobile",
    "Classic Ceramic Piggy Money Bank",
    "Wooden Chess & Board Game Set",
]

# Helper to download image from Unsplash source
def download_image(query, dest_path):
    # Using Unsplash source endpoint which redirects to a random matching image
    url = f"https://source.unsplash.com/1000x1000/?{query.replace(' ', '%20')}"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            with open(dest_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"Failed to download {query}: status {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {query}: {e}")
        return False

# Load catalog
with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

updated = 0
for product in catalog:
    name = product.get('name')
    if name in TARGET_NAMES:
        prod_id = product['id']
        img_filename = f"toy_{prod_id}_real.jpg"
        img_path = STATIC_IMG_DIR / img_filename
        success = download_image(name, img_path)
        if success:
            # Update image path relative to static folder
            product['image'] = f"/static/toys_final/{img_filename}"
            updated += 1
        else:
            print(f"Could not fetch image for {name}")

if updated:
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=4, ensure_ascii=False)
    print(f"Updated images for {updated} products.")
else:
    print("No matching products updated.")
