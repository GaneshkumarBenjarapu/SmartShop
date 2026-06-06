import json
import os
import random
import glob

def get_base_shape(type_str, fill_color):
    if type_str == 'tshirt':
        # Simple T-shirt
        return f'<path d="M 200,100 L 600,100 L 800,300 L 650,400 L 650,800 L 150,800 L 150,400 L 0,300 Z" fill="{fill_color}"/>'
    elif type_str == 'shirt':
        # Collared shirt
        return f'''
        <path d="M 200,100 L 600,100 L 800,300 L 650,400 L 650,800 L 150,800 L 150,400 L 0,300 Z" fill="{fill_color}"/>
        <path d="M 200,100 L 400,200 L 600,100 Z" fill="#ffffff" opacity="0.3"/>
        <line x1="400" y1="200" x2="400" y2="800" stroke="#000000" stroke-width="5" opacity="0.4"/>
        '''
    elif type_str == 'jeans':
        # Jeans
        return f'''
        <path d="M 250,100 L 550,100 L 600,300 L 700,850 L 450,850 L 400,450 L 350,850 L 100,850 L 200,300 Z" fill="{fill_color}"/>
        <line x1="400" y1="100" x2="400" y2="450" stroke="#ffffff" stroke-width="4" stroke-dasharray="10,10"/>
        '''
    elif type_str == 'trousers':
        # Trousers
        return f'''
        <path d="M 250,100 L 550,100 L 580,300 L 650,850 L 420,850 L 400,400 L 380,850 L 150,850 L 220,300 Z" fill="{fill_color}"/>
        <line x1="250" y1="150" x2="550" y2="150" stroke="#000" stroke-width="3" opacity="0.2"/>
        '''

def generate_svg(pid, name):
    name_low = name.lower()
    if 't-shirt' in name_low or 'tshirt' in name_low:
        type_str = 'tshirt'
    elif 'shirt' in name_low:
        type_str = 'shirt'
    elif 'jeans' in name_low or 'denim' in name_low:
        type_str = 'jeans'
    else:
        type_str = 'trousers'

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFD166', '#D4A5A5', '#9B59B6', '#3498DB', '#E67E22', '#2ECC71', '#F1C40F', '#1ABC9C']
    bg_color = '#F8F9FA'
    # Use product ID as random seed so it's consistent
    random.seed(pid)
    fill_color = random.choice(colors)

    svg = f'''<?xml version="1.0" encoding="utf-8"?>
<svg width="800" height="1000" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="{bg_color}"/>
  <g transform="translate(0, 20)">
      {get_base_shape(type_str, fill_color)}
  </g>
  <rect x="0" y="850" width="800" height="150" fill="#2d3436"/>
  <text x="400" y="915" font-family="Arial, sans-serif" font-size="34" fill="white" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="400" y="960" font-family="Arial, sans-serif" font-size="20" fill="#b2bec3" text-anchor="middle">Men Fashion - Item ID: {pid}</text>
  
  <text x="780" y="30" font-family="Arial" font-size="16" fill="#dfe6e9" text-anchor="end">SmartShop Exclusive</text>
</svg>
'''
    filename = f'men_{pid}_{type_str}.svg'
    filepath = f'frontend/static/{filename}'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(svg)
    return f'/static/{filename}'

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'men fashion':
        pid = p['id']
        local_files = glob.glob(f'frontend/static/men_{pid}_*.png')
        if local_files:
            filename = os.path.basename(local_files[0])
            p['image'] = f'/static/{filename}'
        else:
            # Generate unique SVG!
            p['image'] = generate_svg(pid, p['name'])

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("SVGs generated successfully.")
