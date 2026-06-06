import json
import urllib.request
import os
import time

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

pointers = {'action figure': 0, 'block': 0, 'board game': 0, 'puzzle': 0}

with open('data/catalog.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    if p.get('category', '').lower() == 'toys':
        pid = p['id']
        path = f'frontend/static/toy_real_{pid}.jpg'
        
        name_low = p['name'].lower()
        cat_key = 'block'
        if 'action figure' in name_low: cat_key = 'action figure'
        elif 'board game' in name_low: cat_key = 'board game'
        elif 'puzzle' in name_low: cat_key = 'puzzle'
        
        arr = blocks
        if cat_key == 'action figure': arr = action_figures
        elif cat_key == 'board game': arr = board_games
        elif cat_key == 'puzzle': arr = puzzles
        
        img_url = arr[pointers[cat_key] % len(arr)]
        pointers[cat_key] += 1
        
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            print(f"Fixing missing toy {pid}: {p['name']} -> {img_url}")
            try:
                time.sleep(2.5)  # Strict delay to prevent Wikipedia 429
                req = urllib.request.Request(img_url, headers={'User-Agent': f'CoolShopBot_{pid}/1.0'})
                with urllib.request.urlopen(req, timeout=30) as response, open(path, 'wb') as out_file:
                    out_file.write(response.read())
                
                p['image'] = f"/static/toy_real_{pid}.jpg"
                print("Success")
            except Exception as e:
                print(f"Failed again on {img_url}: {e}")
        else:
            p['image'] = f"/static/toy_real_{pid}.jpg"

with open('data/catalog.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Finished fixing missing toys.")
