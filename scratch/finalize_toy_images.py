import os
import json
import shutil
import glob

def setup_toys():
    d = 'frontend/static/toys_final'
    os.makedirs(d, exist_ok=True)
    
    # 1. Copy the 5 generated images from brain folder
    brain_dir = r"C:\Users\DELL\.gemini\antigravity\brain\6e9e055c-9d33-44c5-b221-252338d52b77"
    generated = {
        173: "toy_173_blocks_*.png",
        174: "toy_174_kitchen_*.png",
        175: "toy_175_teddy_*.png",
        176: "toy_176_doctor_*.png",
        177: "toy_177_trucks_*.png"
    }
    
    image_paths = {}
    
    for pid, pattern in generated.items():
        matches = glob.glob(os.path.join(brain_dir, pattern))
        if matches:
            src = matches[0]
            dst = os.path.join(d, f"toy_{pid}.png")
            shutil.copyfile(src, dst)
            image_paths[pid] = f"/static/toys_final/toy_{pid}.png"
            
    # 2. Assign amazon toy images to the remaining 10
    amazon_images = sorted(glob.glob("frontend/static/amazon_toy_*.jpg"))
    remaining_pids = [178, 179, 180, 181, 182, 183, 184, 185, 186, 187]
    
    for i, pid in enumerate(remaining_pids):
        if i < len(amazon_images):
            src = amazon_images[i]
            dst = os.path.join(d, f"toy_{pid}.jpg")
            shutil.copyfile(src, dst)
            image_paths[pid] = f"/static/toys_final/toy_{pid}.jpg"

    # 3. Update catalog
    with open('data/catalog.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for p in data:
        if p.get('category') == 'Toys':
            pid = p.get('id')
            if pid in image_paths:
                p['image'] = image_paths[pid]

    with open('data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print("Catalog updated with new AI-generated and premium Amazon toy images.")

if __name__ == '__main__':
    setup_toys()
