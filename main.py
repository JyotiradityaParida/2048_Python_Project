import time
from board import create_board, print_board
from game_logic import add_random_tile, move_board, check_game_over
from file_manager import save_game, load_game, load_highscore, save_highscore

def get_key():
    k = input("Move (W/A/S/D K=Save L=Load Q=Quit P=Reset HS): ").lower().strip()
    if k in ("w","a","s","d","k","l","q","p"):
        return k
    return None

board = create_board()
add_random_tile(board)
add_random_tile(board)
moves = 0
score = 0
f = True
high = load_highscore()
w = len("+------"*4 + "+")

while True:

    print("************2048************")
    print()
    print_board(board)
    print()
    print(f"Score: {score}   Moves: {moves}   High Score: {high}")
    print()

    key = get_key()

    print()

    if not key:
        continue

    if key == "q":
        print("THANKS FOR PLAYING")
        print()
        print("*" * w)
        time.sleep(1)
        break

    if key in ("w","a","s","d"):
        moved, gained = move_board(board, key)
        if moved:
            score += gained
            moves += 1
            add_random_tile(board)
            if score > high:
                high = score
                save_highscore(high)
            if any(2048 in row for row in board) and f==True:
                f = False
                print("************2048************")
                print()
                print_board(board)
                print()
                print("="*w)
                print()
                print(" VICTORY!! YOU REACHED 2048! ")
                print()
                print("="*w)
                print()
                time.sleep(1)
            

    elif key == "k":
        save_game(board, score, moves)
        print("SAVED")
        time.sleep(1)
        continue

    elif key == "l":
        g = load_game()
        if g:
            board, score, moves = g
            print("LOADED")
        else:
            print("NO SAVE FOUND")
        time.sleep(1)
        continue

    elif key == "p":
        high = 0
        save_highscore(0)
        print("HIGH SCORE RESET")
        continue

    if check_game_over(board):
        print("************2048************")
        print()
        print_board(board)
        print()
        print("GAME OVER")
        print(f"Final Score: {score}   Final Moves: {moves}   High: {high}")
        print("*" * w)
        break