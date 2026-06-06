import json

out = []
with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    category = p.get('category', '').lower()
    img = p.get('image', '')
    if 'men fashion' in category:
        out.append(f"{p['id']}: {p['name']} | MEN FASHION | {img}")
    else:
        out.append(f"{p['id']}: {p['name']} | OTHER ({category}) | {img}")

with open('scratch/catalog_dump.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Dumped to scratch/catalog_dump.txt")
