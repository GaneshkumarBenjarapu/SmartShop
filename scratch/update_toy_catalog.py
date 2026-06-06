import json

def update_catalog_toys():
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('category') == 'Toys':
            p['image'] = f"/static/toys_v5/toy_{p['id']}_meesho_v2.png"

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print("Catalog updated with new toy images.")

if __name__ == '__main__':
    update_catalog_toys()
