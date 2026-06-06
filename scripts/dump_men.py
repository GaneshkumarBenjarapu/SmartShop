import json

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    cat = p.get('category', '').lower()
    if cat == 'men fashion':
        print(f"{p['id']}: {p['name']} | {p['image']}")
