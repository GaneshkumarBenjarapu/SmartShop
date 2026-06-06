import json

image_map = {
    60: "https://images.unsplash.com/photo-1581655353564-df123a1eb820?q=80&w=1000&auto=format&fit=crop", # Polo T-Shirt
    61: "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=1000&auto=format&fit=crop", # Levi's Jeans
    62: "https://images.unsplash.com/photo-1596755094514-f8b1e4c70fba?q=80&w=1000&auto=format&fit=crop", # Casual Shirt
    63: "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=1000&auto=format&fit=crop", # Formal Trousers
    143: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?q=80&w=1000&auto=format&fit=crop", # Crew Neck T-Shirt
    144: "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?q=80&w=1000&auto=format&fit=crop", # Chino Trousers
    145: "https://images.unsplash.com/photo-1602810318383-e386cc2a3ce3?q=80&w=1000&auto=format&fit=crop", # Formal Shirt
    146: "https://images.unsplash.com/photo-1604176354204-9268738cb284?q=80&w=1000&auto=format&fit=crop", # Regular Fit Jeans
    147: "https://images.unsplash.com/photo-1576566588028-4147f3842f27?q=80&w=1000&auto=format&fit=crop", # Essential Logo T-Shirt
    148: "https://images.unsplash.com/photo-1555689502-c4b22d76c56f?q=80&w=1000&auto=format&fit=crop", # Cotton Chino Pants
    149: "https://images.unsplash.com/photo-1506629082955-511b1aa562c8?q=80&w=1000&auto=format&fit=crop", # Slim Fit Casual Trousers
    150: "https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?q=80&w=1000&auto=format&fit=crop", # Solid Polo T-Shirt
    151: "https://images.unsplash.com/photo-1510312480391-768ad8b857dc?q=80&w=1000&auto=format&fit=crop", # Cargo Trousers
    152: "https://images.unsplash.com/photo-1582552938357-32b906df40cb?q=80&w=1000&auto=format&fit=crop", # Tapered Fit Denim Jeans
    153: "https://images.unsplash.com/photo-1503342394128-c104d54dba01?q=80&w=1000&auto=format&fit=crop", # Typography Printed T-Shirt
    154: "https://images.unsplash.com/photo-1588359348347-9bc6cbbb689e?q=80&w=1000&auto=format&fit=crop", # Checked Casual Shirt
    155: "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?q=80&w=1000&auto=format&fit=crop", # Solid Round Neck T-Shirt
    156: "https://images.unsplash.com/photo-1559582798-678dfc71caf8?q=80&w=1000&auto=format&fit=crop", # Slim Fit Chino Trousers
    157: "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?q=80&w=1000&auto=format&fit=crop", # Straight Fit Jeans
    9004: "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1000&auto=format&fit=crop", # Breasted Blazer
    9005: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=1000&auto=format&fit=crop" # Leather Office Briefcase
}

def update_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    count = 0
    for p in data:
        if p.get('category', '').lower() == 'men fashion' and p.get('id') in image_map:
            p['image'] = image_map[p['id']]
            count += 1

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Updated {count} products in data/catalog.json with unique Unsplash images.")

if __name__ == '__main__':
    update_catalog()
