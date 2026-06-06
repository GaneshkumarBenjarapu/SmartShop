import os
import json
import shutil

def fix_toy_images():
    d = 'frontend/static/toys_final'
    os.makedirs(d, exist_ok=True)
    
    # 1. Update catalog
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('category') == 'Toys':
            pid = p.get('id')
            
            # For 178-187, use the toy_real_{pid}.jpg which matches the product name perfectly
            if pid >= 178 and pid <= 187:
                src = f"frontend/static/toy_real_{pid}.jpg"
                dst = f"frontend/static/toys_final/toy_{pid}.jpg"
                
                if os.path.exists(src):
                    shutil.copyfile(src, dst)
                    p['image'] = f"/static/toys_final/toy_{pid}.jpg"
                    print(f"Fixed image for {pid}: {p['name']}")
                else:
                    print(f"WARNING: Missing real image for {pid}")

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print("Catalog updated with matching real images.")

if __name__ == '__main__':
    fix_toy_images()
