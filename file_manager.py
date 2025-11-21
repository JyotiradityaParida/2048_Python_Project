import os, json

DATA_FOLDER = "data"
SAVE_FILE = os.path.join(DATA_FOLDER, "2048_save.txt")
HS_FILE = os.path.join(DATA_FOLDER, "highscore.txt")

if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def save_game(board, score, moves):
    with open(SAVE_FILE,"w") as f:
        json.dump({"board":board,"score":score,"moves":moves},f)

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None
    d = json.load(open(SAVE_FILE))
    return d["board"], d["score"], d["moves"]

def load_highscore():
    if os.path.exists(HS_FILE):
        return int(open(HS_FILE).read().strip())
    return 0

def save_highscore(v):
    open(HS_FILE,"w").write(str(v))