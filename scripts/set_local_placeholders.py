import json, os
root = os.path.dirname(os.path.dirname(__file__))
cat = os.path.join(root, 'catalog.json')
with open(cat, 'r', encoding='utf-8') as f:
    data = json.load(f)

mapping = {
    'Electronics': '/static/placeholders/electronics.svg',
    'Books': '/static/placeholders/books.svg',
    'Shoes': '/static/placeholders/shoes.svg',
    'Toys': '/static/placeholders/toys.svg',
    'Beauty': '/static/placeholders/beauty.svg',
    'Home Appliances': '/static/placeholders/home_appliances.svg',
    'Men Fashion': '/static/placeholders/clothing.svg',
    'Women Fashion': '/static/placeholders/clothing.svg',
    'Kidsware': '/static/placeholders/clothing.svg',
    'Clothing': '/static/placeholders/clothing.svg'
}
changed = 0
for p in data:
    catname = p.get('category') or ''
    placeholder = mapping.get(catname, '/static/placeholders/default.svg')
    if p.get('image') != placeholder or p.get('images') != [placeholder]:
        p['image'] = placeholder
        p['images'] = [placeholder]
        changed += 1

with open(cat, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
print('Updated', changed, 'products to local placeholders')
