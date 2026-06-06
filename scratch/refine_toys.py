import json

def modify_toys():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Remove similar/redundant products
    # IDs to remove: 186 (Duplicate LEGO), 177 (Operation), 179 (Trouble), 182 (Battleship)
    ids_to_remove = {186, 177, 179, 182}
    data = [p for p in data if p.get('id') not in ids_to_remove]

    # 2. Add new products: Soft Toys, Cars, Music Toys
    new_toys = [
        {
            "id": 188,
            "name": "Giant Plush Teddy Bear",
            "price": 1200,
            "description": "Ultra-soft and cuddly 3-foot teddy bear.",
            "category": "Toys",
            "rating": 4.8,
            "image": "",
            "color": "brown",
            "brand": "SoftCuddles",
            "size": "large",
            "discount": 10
        },
        {
            "id": 189,
            "name": "Cuddly Plush Elephant",
            "price": 800,
            "description": "Soft plush elephant for babies and toddlers.",
            "category": "Toys",
            "rating": 4.7,
            "image": "",
            "color": "grey",
            "brand": "SoftCuddles",
            "size": "medium",
            "discount": 15
        },
        {
            "id": 190,
            "name": "High-Speed Remote Control Racing Car",
            "price": 2500,
            "description": "1:14 scale RC car with rechargeable batteries.",
            "category": "Toys",
            "rating": 4.5,
            "image": "",
            "color": "red",
            "brand": "SpeedX",
            "size": "medium",
            "discount": 20
        },
        {
            "id": 191,
            "name": "Die-cast Metal Sports Car Set (5-Pack)",
            "price": 1500,
            "description": "Collection of 5 premium metal sports cars.",
            "category": "Toys",
            "rating": 4.6,
            "image": "",
            "color": "multi",
            "brand": "SpeedX",
            "size": "small",
            "discount": 5
        },
        {
            "id": 192,
            "name": "Kids 37-Key Electronic Keyboard Piano",
            "price": 3200,
            "description": "Digital piano with microphone and recording.",
            "category": "Toys",
            "rating": 4.4,
            "image": "",
            "color": "black",
            "brand": "MelodyKids",
            "size": "medium",
            "discount": 10
        },
        {
            "id": 193,
            "name": "Wooden Xylophone for Kids",
            "price": 600,
            "description": "Classical musical toy with 8 colorful keys.",
            "category": "Toys",
            "rating": 4.9,
            "image": "",
            "color": "multi",
            "brand": "MelodyKids",
            "size": "small",
            "discount": 0
        },
        {
            "id": 194,
            "name": "Toddler Jazz Drum Set",
            "price": 1800,
            "description": "Complete drum set with stool and cymbals.",
            "category": "Toys",
            "rating": 4.3,
            "image": "",
            "color": "blue",
            "brand": "MelodyKids",
            "size": "medium",
            "discount": 25
        }
    ]

    # Generate images for new toys using the same Pollinations logic
    import urllib.parse
    for p in new_toys:
        prompt = f"Professional studio photography of {p['name']}, bright cinematic lighting, high-end toy packaging style, isolated on clean white background, 8k resolution, vibrant colors, premium quality product shot"
        encoded_prompt = urllib.parse.quote(prompt)
        seed = p['id'] * 98765
        p['image'] = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&nologo=true&seed={seed}"

    data.extend(new_toys)

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Removed {len(ids_to_remove)} toys and added {len(new_toys)} new toys.")

if __name__ == '__main__':
    modify_toys()
