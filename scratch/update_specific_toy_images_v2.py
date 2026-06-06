import json
import os
from pathlib import Path

# Ensure Pillow is available; if not, we can use basic image generation via base64 placeholder
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    raise ImportError('Pillow library is required for image generation')

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]  # project root (Product recommendation)
CATALOG_PATH = r"c:/Users/DELL/OneDrive/Desktop/Product recommendation/data/catalog.json"
STATIC_IMG_DIR = BASE_DIR / 'frontend' / 'static' / 'toys_fresh'
STATIC_IMG_DIR.mkdir(parents=True, exist_ok=True)

# Target products (IDs may vary; we'll search by name)
TARGET_NAMES = [
    "Creative Arts & Crafts Slime Kit",
    "Musical Learning Toy Mobile",
    "Classic Ceramic Piggy Money Bank",
    "Wooden Chess & Board Game Set",
]

# Load catalog
with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

updated = 0
for product in catalog:
    if product.get('name') in TARGET_NAMES:
        prod_id = product['id']
        # Create a simple placeholder image with product name
        img_path = STATIC_IMG_DIR / f'toy_{prod_id}_fresh.png'
        # Create image 1000x1000 solid background with text
        img = Image.new('RGB', (1000, 1000), color=(200, 220, 255))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype('arial.ttf', 40)
        except Exception:
            font = ImageFont.load_default()
        text = product['name']

        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        draw.text(((1000 - text_w) / 2, (1000 - text_h) / 2), text, fill='black', font=font)

        img.save(img_path)
        # Update catalog image path (relative to static folder)
        product['image'] = f'/static/toys_fresh/{img_path.name}'
        updated += 1

if updated:
    # Write back catalog
    with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=4, ensure_ascii=False)
    print(f'Updated images for {updated} products.')
else:
    print('No matching products found to update.')
