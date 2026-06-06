import json
import urllib.request
import os

action_figures = [
    'https://upload.wikimedia.org/wikipedia/commons/1/12/ExpoBatman20220917_ohs33.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/a/ae/Fashion_action_figure.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/6/6a/Greeting-figure-in-mirror.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/3a/Soldier_action_figures.jpg'
]

blocks = [
    'https://upload.wikimedia.org/wikipedia/commons/6/65/LEGO_handcuff.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/0/0a/Lego_in_1957.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/4/45/Pile_of_light_gray_LEGO_bricks_at_a_LEGO_store.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/9/90/Simple_lego_bike.jpg'
]

board_games = [
    'https://upload.wikimedia.org/wikipedia/commons/d/df/German_Monopoly_board_in_the_middle_of_a_game.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/c/cc/Monopoly_board_game.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/7/78/Monopoly_board_on_white_bg.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/3/33/RSVP_word_game_by_Scrabble_%282837597425%29.jpg'
]

puzzles = [
    'https://upload.wikimedia.org/wikipedia/commons/6/66/Jigsaw_puzzle_01_by_Scouten.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/11/Jigsaw_puzzle_in_progress.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/c/c4/Jigsaw_puzzle_solving_2.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/4/49/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall_-_1000_piece_jigsaw_puzzle.jpg'
]

def pop_image(arr):
    return arr.pop(0) if len(arr) > 0 else 'https://upload.wikimedia.org/wikipedia/commons/0/0a/Lego_in_1957.jpg'

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        pid = p['id']
        name_low = p['name'].lower()
        img_url = ''
        
        if 'action figure' in name_low:
            img_url = pop_image(action_figures)
        elif 'block' in name_low:
            img_url = pop_image(blocks)
        elif 'board game' in name_low:
            img_url = pop_image(board_games)
        elif 'puzzle' in name_low:
            img_url = pop_image(puzzles)
        else:
            img_url = pop_image(blocks)
            
        local_name = f"toy_real_{pid}.jpg"
        local_path = os.path.join('frontend', 'static', local_name)
        
        try:
            print(f"Downloading {img_url} to {local_name}...")
            req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=20) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
            
            p['image'] = f"/static/{local_name}"
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Toys updated to unique Wikimedia images and saved locally!")
