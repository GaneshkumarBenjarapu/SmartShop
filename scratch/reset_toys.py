import json, os

CATALOG_PATH = 'data/catalog.json'

# Load existing catalog
with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Remove existing toys
data = [p for p in data if p.get('category') != 'Toys']

# Determine next id
def next_id(start=200):
    max_id = max([p['id'] for p in data] + [0])
    return max(max_id + 1, start)

new_toys = [
    {
        'id': next_id(),
        'name': 'Squeaky Animal Plush Bear',
        'price': 299,
        'description': 'Soft plush bear with squeaky sound for kids.',
        'category': 'Toys',
        'rating': 4.7,
        'image': f'https://source.unsplash.com/1000x1000/?toy,plush,bear&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'brown',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 10
    },
    {
        'id': next_id(),
        'name': 'Wooden Building Blocks Set',
        'price': 399,
        'description': 'Eco-friendly wooden blocks for creative building.',
        'category': 'Toys',
        'rating': 4.8,
        'image': f'https://source.unsplash.com/1000x1000/?toy,blocks,wooden&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'multicolor',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 5
    },
    {
        'id': next_id(),
        'name': 'Kids Musical Keyboard',
        'price': 549,
        'description': 'Mini keyboard with lights and preset songs.',
        'category': 'Toys',
        'rating': 4.6,
        'image': f'https://source.unsplash.com/1000x1000/?toy,keyboards,music&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'black',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 15
    },
    {
        'id': next_id(),
        'name': 'Remote Control Racing Car',
        'price': 799,
        'description': 'Fast RC car with rechargeable battery.',
        'category': 'Toys',
        'rating': 4.5,
        'image': f'https://source.unsplash.com/1000x1000/?toy,rc,car&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'red',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 12
    },
    {
        'id': next_id(),
        'name': 'DIY Craft Slime Kit',
        'price': 199,
        'description': 'All ingredients to create colorful slime.',
        'category': 'Toys',
        'rating': 4.3,
        'image': f'https://source.unsplash.com/1000x1000/?toy,slime,craft&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'green',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 8
    },
    {
        'id': next_id(),
        'name': 'Pretend Kitchen Play Set',
        'price': 449,
        'description': 'Mini pots, pans and accessories for role‑play cooking.',
        'category': 'Toys',
        'rating': 4.7,
        'image': f'https://source.unsplash.com/1000x1000/?toy,kitchen,play&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'white',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 10
    },
    {
        'id': next_id(),
        'name': 'Educational Puzzle Globe',
        'price': 349,
        'description': 'World map puzzle to teach geography.',
        'category': 'Toys',
        'rating': 4.6,
        'image': f'https://source.unsplash.com/1000x1000/?toy,puzzle,globe&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'blue',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 7
    },
    {
        'id': next_id(),
        'name': 'Soft Plush Bunny',
        'price': 259,
        'description': 'Cuddly bunny plush toy for bedtime.',
        'category': 'Toys',
        'rating': 4.8,
        'image': f'https://source.unsplash.com/1000x1000/?toy,bunny,plush&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'white',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 5
    },
    {
        'id': next_id(),
        'name': 'Miniature Tool Set',
        'price': 299,
        'description': 'Kids'"'"'s tool bench with plastic tools.',
        'category': 'Toys',
        'rating': 4.4,
        'image': f'https://source.unsplash.com/1000x1000/?toy,tool,kit&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'yellow',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 9
    },
    {
        'id': next_id(),
        'name': 'Bubble Gun Toy',
        'price': 199,
        'description': 'Battery‑operated bubble gun for outdoor fun.',
        'category': 'Toys',
        'rating': 4.2,
        'image': f'https://source.unsplash.com/1000x1000/?toy,bubble,gun&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'blue',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 6
    },
    {
        'id': next_id(),
        'name': 'Water Ring Toss Game',
        'price': 149,
        'description': 'Indoor water ring toss for kids.',
        'category': 'Toys',
        'rating': 4.1,
        'image': f'https://source.unsplash.com/1000x1000/?toy,ring,toss&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'transparent',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 4
    },
    {
        'id': next_id(),
        'name': 'Mini Puzzle Animal Set',
        'price': 179,
        'description': 'Puzzle pieces forming various animals.',
        'category': 'Toys',
        'rating': 4.3,
        'image': f'https://source.unsplash.com/1000x1000/?toy,animal,puzzle&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'multicolor',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 7
    },
    {
        'id': next_id(),
        'name': 'Kids Drawing Board',
        'price': 239,
        'description': 'Magnetic drawing board for doodling.',
        'category': 'Toys',
        'rating': 4.5,
        'image': f'https://source.unsplash.com/1000x1000/?toy,drawing,board&sig={next_id()}',
        'badge_class': '',
        'badge_icon': '',
        'badge_text': '',
        'color': 'white',
        'brand': 'Meesho',
        'size': 'standard',
        'discount': 10
    }
]

# Append new toys to catalog
data.extend(new_toys)

# Save back
with open(CATALOG_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f'Added {len(new_toys)} new toy products. Catalog updated.')
