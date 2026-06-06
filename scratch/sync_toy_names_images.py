import json
import os

def fix_toy_catalog_completely():
    # Load catalog
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remove existing Toys
    data = [p for p in data if p.get('category') != 'Toys']
    
    # Define perfect list of toys that matches our available images
    perfect_toys = [
        (173, "Wooden Alphabet Learning Blocks", 249, "/static/toys_final/toy_173.png"),
        (174, "Complete Kitchen Pretend Play Set", 499, "/static/toys_final/toy_174.png"),
        (175, "Premium Soft Plush Teddy Bear", 349, "/static/toys_final/toy_175.png"),
        (176, "Kids Medical Doctor Case Toy", 399, "/static/toys_final/toy_176.png"),
        (177, "Construction Truck Set (Pack of 3)", 549, "/static/toys_final/toy_177.png"),
        (178, "Creative Arts & Crafts Slime Kit", 199, "/static/toys_final/toy_178.jpg"),
        (179, "Musical Learning Toy Mobile", 299, "/static/toys_final/toy_179.jpg"),
        (180, "Classic Ceramic Piggy Money Bank", 149, "/static/toys_final/toy_180.jpg"),
        (181, "Wooden Chess & Board Game Set", 449, "/static/toys_final/toy_181.jpg"),
        (182, "Soft Plush Bunny Rabbit Toy", 199, "/static/toys_final/toy_182.jpg"),
        (183, "STEM Junior Science Experiment Kit", 699, "/static/toys_final/toy_183.jpg"),
        (184, "Mega Building Blocks (120 Pieces)", 599, "/static/toys_final/toy_184.jpg"),
        (185, "Interactive Educational Game Board", 349, "/static/toys_final/toy_185.jpg"),
        (186, "Automatic Bubble Blaster Gun", 249, "/static/toys_final/toy_186.jpg"),
        (187, "Jenga Style Wooden Stacking Game", 299, "/static/toys_final/toy_187.jpg")
    ]
    
    for pid, name, price, img_path in perfect_toys:
        data.append({
            "id": pid,
            "name": name,
            "price": price,
            "description": f"Premium high-quality {name} for kids.",
            "category": "Toys",
            "rating": 4.6,
            "image": img_path,
            "brand": "ToyBrand",
            "color": "multi",
            "size": "standard",
            "discount": 10
        })

    # Save catalog
    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print("Catalog updated with perfectly matching names and images.")

if __name__ == '__main__':
    fix_toy_catalog_completely()
