"""
file_manager.py
----------------
handles saving and loading persistent game data
- board state
- score and move count
- RNG state (for reproducible tile spawning)
- high score storage

Creates the data/directory automatically if missing.
"""

import os,json,random

# Connecting the data folder to the save and high score files.
DATA_FOLDER = "data"
SAVE_FILE = os.path.join(DATA_FOLDER, "2048_save.txt")
HS_FILE = os.path.join(DATA_FOLDER, "highscore.txt")

# Creating the data folder if it doesnt already exist.
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

# Function to save game data (board,score,moves)
def save_game(board, score, moves):
    with open(SAVE_FILE, "w") as f:
        json.dump({
            "board": board,
            "score": score,
            "moves": moves,
            "rng_state": repr(random.getstate())   # save RNG
        }, f)


# Function to load game data.
def load_game():
    if not os.path.exists(SAVE_FILE):               #if saved game not found
        return None
    d = json.load(open(SAVE_FILE))

    # restore RNG state if saved
    if "rng_state" in d:
        random.setstate(eval(d["rng_state"]))

    return d["board"], d["score"], d["moves"]


# Function to load highscore.
def load_highscore():
    if os.path.exists(HS_FILE):
        return int(open(HS_FILE).read().strip())
    return 0

# Function to save highscore.
def save_highscore(v):
    open(HS_FILE,"w").write(str(v))
