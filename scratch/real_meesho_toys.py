import urllib.request
import os
import json

d = 'frontend/static/toys_meesho'
os.makedirs(d, exist_ok=True)

# 15 Real, high-quality Unsplash photos representing Meesho toys
meesho_toy_data = [
    (173, "Wooden Alphabet Learning Blocks", 249, "1560419015-7c427e8ae5ba"),
    (174, "Complete Kitchen Pretend Play Set", 499, "1516627145497-ae6968895b74"),
    (175, "Premium Soft Plush Teddy Bear", 349, "1590483734731-030616149495"),
    (176, "Kids Medical Doctor Case Toy", 399, "1616137422495-1e902b72174c"),
    (177, "Construction Truck Set (Pack of 3)", 549, "1594731802114-173873495079"),
    (178, "Creative Arts & Crafts Slime Kit", 199, "1513364776144-60967b0f800f"),
    (179, "Musical Learning Toy Mobile", 299, "1516280440614-37939bbacd81"),
    (180, "Classic Ceramic Piggy Money Bank", 149, "1629904853716-f0bc54eba481"),
    (181, "Wooden Chess & Board Game Set", 449, "1529699211952-734e80c4d42b"),
    (182, "Soft Plush Bunny Rabbit Toy", 199, "1615486511484-92e172cc4fe0"),
    (183, "STEM Junior Science Experiment Kit", 699, "1530210124550-912dc1381cb8"),
    (184, "Mega Building Blocks (120 Pieces)", 599, "1587654780288-6b280ce0eb82"),
    (185, "Interactive Educational Game Board", 349, "1611891487122-207579d67d98"),
    (186, "Automatic Bubble Blaster Gun", 249, "1511884642898-4c92249e20b6"),
    (187, "Jenga Style Wooden Stacking Game", 299, "1510070112810-d4e9a46d9e91")
]

def download_images():
    for pid, name, price, photo_id in meesho_toy_data:
        fname = f"toy_{pid}_real.png"
        fpath = os.path.join(d, fname)
        
        # Use Unsplash primarily, fallback to LoremFlickr for known 404s
        if pid in [175, 176, 177, 180, 184]:
            keywords = name.lower().replace(' ', ',')
            url = f"https://loremflickr.com/1000/1000/{keywords}/all?lock={pid}"
        else:
            url = f"https://images.unsplash.com/photo-{photo_id}?q=80&w=1000&auto=format&fit=crop"
        
        try:
            print(f"Downloading real image for {name} from {url}...")
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=15) as res, open(fpath, 'wb') as f_out:
                f_out.write(res.read())
            print(f"Saved {fname}")
        except Exception as e:
            print(f"Failed {pid}: {e}")

def update_catalog():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Remove old toys and add new ones
    data = [p for p in data if p.get('category') != 'Toys']
    
    for pid, name, price, _ in meesho_toy_data:
        data.append({
            "id": pid,
            "name": name,
            "price": price,
            "description": f"Best selling Meesho-style {name} for kids.",
            "category": "Toys",
            "rating": 4.5,
            "image": f"/static/toys_meesho/toy_{pid}_real.png",
            "brand": "MeeshoSelection",
            "color": "multi",
            "size": "standard",
            "discount": 10
        })

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Catalog updated with real Meesho toy products and images.")

if __name__ == '__main__':
    download_images()
    update_catalog()
