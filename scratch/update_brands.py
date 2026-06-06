import json
import os

catalog_path = 'data/catalog.json'
with open(catalog_path, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

lg_ids = {15, 51, 201, 202, 203, 204, 205}
bluestar_ids = {52, 206, 207, 208, 209, 210}

updated_count = 0
for p in catalog:
    pid = p.get('id')
    if pid in lg_ids:
        p['brand'] = 'lg'
        updated_count += 1
    elif pid in bluestar_ids:
        p['brand'] = 'bluestar'
        updated_count += 1

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=4)

print(f"Updated brands for {updated_count} products.")
