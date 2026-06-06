import json
import urllib.parse

def replace_with_meesho_toys():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Remove all existing Toys
    data = [p for p in data if p.get('category') != 'Toys']

    # 2. Define Meesho Toy Products
    meesho_toys = [
        {"id": 173, "name": "Educational Wooden Alphabet Puzzle", "price": 299, "description": "Colorful wooden alphabet puzzle for early learning.", "category": "Toys", "rating": 4.5, "brand": "MeeshoHome", "color": "multi"},
        {"id": 174, "name": "Electronic Dancing Cactus with Recording", "price": 449, "description": "Sings, dances, and mimics what you say.", "category": "Toys", "rating": 4.2, "brand": "TrendToys", "color": "green"},
        {"id": 175, "name": "Reversible Octopus Soft Toy", "price": 199, "description": "Express your mood with this reversible plush.", "category": "Toys", "rating": 4.8, "brand": "MeeshoHome", "color": "blue-pink"},
        {"id": 176, "name": "2-in-1 Magnetic Writing & Drawing Board", "price": 349, "description": "Erasable magnetic board for creative kids.", "category": "Toys", "rating": 4.4, "brand": "LearnSmart", "color": "blue"},
        {"id": 177, "name": "Friction Powered Heavy Duty Truck Set", "price": 599, "description": "Set of 3 construction trucks for indoor play.", "category": "Toys", "rating": 4.3, "brand": "RuggedPlay", "color": "yellow"},
        {"id": 178, "name": "DIY Crystal Slime Making Kit", "price": 249, "description": "Make your own colorful crystal slime at home.", "category": "Toys", "rating": 4.1, "brand": "TrendToys", "color": "multi"},
        {"id": 179, "name": "Miniature Kitchen Set with Accessories", "price": 699, "description": "Complete kitchen set for pretend cooking play.", "category": "Toys", "rating": 4.6, "brand": "MeeshoHome", "color": "pink"},
        {"id": 180, "name": "Complete Doctor Play Set Suitcase", "price": 399, "description": "Portable suitcase with medical tools for kids.", "category": "Toys", "rating": 4.5, "brand": "CareFun", "color": "blue"},
        {"id": 181, "name": "Handheld Water Ring Toss Toy", "price": 99, "description": "Classic nostalgic handheld game for kids.", "category": "Toys", "rating": 4.0, "brand": "MeeshoHome", "color": "transparent"},
        {"id": 182, "name": "Pull-back Mini Racing Cars (Pack of 6)", "price": 149, "description": "Pocket-sized racing cars for high-speed fun.", "category": "Toys", "rating": 4.3, "brand": "SpeedX", "color": "multi"},
        {"id": 183, "name": "Magical Water Drawing Painting Mat", "price": 499, "description": "Mess-free painting with water-filled pens.", "category": "Toys", "rating": 4.7, "brand": "LearnSmart", "color": "multi"},
        {"id": 184, "name": "Bubble Gun Blaster with Solution", "price": 299, "description": "Easy-to-use bubble gun for endless fun.", "category": "Toys", "rating": 4.2, "brand": "JoyPlay", "color": "blue"},
        {"id": 185, "name": "Flying Sensor Induction Helicopter", "price": 549, "description": "Hand-sensor controlled flying toy for indoor fun.", "category": "Toys", "rating": 4.1, "brand": "TrendToys", "color": "red"},
        {"id": 186, "name": "Musical Toy Mobile Phone with Lights", "price": 199, "description": "Educational toy phone with sounds and light-up keys.", "category": "Toys", "rating": 4.3, "brand": "MelodyKids", "color": "yellow"},
        {"id": 187, "name": "Soft Plush Rabbit Toy (Meesho Edition)", "price": 249, "description": "Small, soft, and cute plush rabbit for gifting.", "category": "Toys", "rating": 4.6, "brand": "MeeshoHome", "color": "white"}
    ]

    # Generate images for Meesho toys with authentic marketplace look
    for p in meesho_toys:
        p["size"] = "standard"
        p["discount"] = 10
        # Authentic Meesho marketplace style: mobile photo, home background, realistic
        prompt = f"Authentic mobile phone photo of {p['name']} on a clean floor, bright indoor lighting, Meesho app product listing, realistic, simple, unedited"
        encoded_prompt = urllib.parse.quote(prompt)
        seed = p['id'] * 12345
        p['image'] = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=800&nologo=true&seed={seed}"

    data.extend(meesho_toys)

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Replaced toy catalog with 15 Meesho-style products.")

if __name__ == '__main__':
    replace_with_meesho_toys()
