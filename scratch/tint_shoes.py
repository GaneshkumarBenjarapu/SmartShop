from PIL import Image
import colorsys
import os

def shift_hue(image_path, output_path, hue_shift):
    img = Image.open(image_path).convert('RGBA')
    pixels = img.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a > 0: # Only process non-transparent pixels
                h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)
                
                # If it's somewhat grey/white but not completely black/white, we can boost saturation and shift hue
                # To make it truly colorful, we boost saturation on the lighter parts
                if v > 0.1 and v < 0.95: 
                    s = min(1.0, s + 0.6) # Boost saturation a lot to apply color to grey/white
                    h = (h + hue_shift) % 1.0
                
                new_r, new_g, new_b = colorsys.hsv_to_rgb(h, s, v)
                pixels[x, y] = (int(new_r * 255), int(new_g * 255), int(new_b * 255), a)
                
    img.save(output_path)

base_image = 'frontend/static/shoes/nike_performance_shoes_21.png'
d = 'frontend/static/shoes'

# Verify base image exists
if not os.path.exists(base_image):
    # Try another one
    base_image = 'frontend/static/shoes/shoe_42.png'

print(f"Using base image: {base_image}")

# Products and their hue shifts (0.0 to 1.0)
targets = [
    ("Red Tape Running Shoes 12", "red_tape_running_v3.png", 0.0), # Red
    ("Nike Performance Shoes 21", "nike_performance_shoes_v3.png", 0.6), # Blue
    ("Skechers Athletic Footwear 58", "skechers_athletic_footwear_v3.png", 0.35), # Green
    ("Skechers Casual Kicks 70", "skechers_casual_kicks_v3.png", 0.15), # Yellow
    ("Skechers Walking Sneakers 52", "skechers_walking_sneakers_v3.png", 0.75), # Purple
    ("Skechers Go Walk Shoes", "skechers_go_walk_v3.png", 0.85), # Pink/Magenta
    ("Red Tape Men's Walking Shoes", "red_tape_mens_walking_v3.png", 0.08), # Orange
    ("Nike Running Shoes 97", "nike_running_shoes_97_v3.png", 0.5) # Cyan
]

for name, fname, hue in targets:
    fpath = os.path.join(d, fname)
    print(f"Tinting {name} to {fname} with hue {hue}...")
    shift_hue(base_image, fpath, hue)
    print(f"Saved {fname}")

