"""
main.py
----------------------
-uses functions from the other files game_logic.py, board.py and file_manager.py
-handles the main loop that runs the game
-takes input, tracks and updates the moves and score, checks for victory and game over

"""

import time #using the time.sleep() function to give the user some time to look at the current screen before moving on to the next move
#importing all the functions created in the other files
from board import create_board, print_board
from game_logic import add_random_tile, move_board, check_game_over
from file_manager import save_game, load_game, load_highscore, save_highscore

board = create_board() #creates the board and the first 2 random tiles to start the game
add_random_tile(board)
add_random_tile(board)

moves = 0 #to track the number of moves done
score = 0 #to track the score
f = False #a flag for when the game is won
high = load_highscore() #the current highscore
w = len("+------"*4 + "+") #the width of the board
while True:
    #printing the game screen
    print("************2048************")
    print()
    print_board(board)
    print()
    print(f"Score: {score}   Moves: {moves}   High Score: {high}")
    print()
    #taking the input from the user and checking if its a valid input
    key = input("Move (W/A/S/D K=Save L=Load Q=Quit P=Reset HS): ").lower().strip()
    if key not in ("w","a","s","d","k","l","q","p"):
        key = None
    print()
    if not key: #for the case when we get an invalid input
        continue
    if key == "q": #for when the user wants to stop playing
        print("THANKS FOR PLAYING")
        print()
        print("*" * w)
        print()
        time.sleep(1)
        break
    if key in ("w","a","s","d"): #for when the user wants to make a move on the board
        moved, gained = move_board(board, key) #the moved variable tells us if a move actually happend or not and the gained variable tells us the score gained
        if moved:
            #adding the gained score, incrementing the move count and spawning a new tile if a valid move was made i.e the tiles actually moved
            score += gained
            moves += 1
            add_random_tile(board) #checking and update the score if a new highscore was made
            if score > high:
                high = score
                save_highscore(high)
            if any(2048 in row for row in board) and f==False: #victory check for when a 2048 tile is created
                f = True
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
    elif key == "k": #saving the game
        save_game(board, score, moves)
        print("SAVED")
        time.sleep(1)
        continue
    elif key == "l": #loading a previously saved game onto the board
        g = load_game()
        if g: #checking if there is a game saved beforehand otherwise giving the error
            board, score, moves = g
            print("LOADED")
            print()
        else:
            print("NO SAVE FOUND")
            print()
        time.sleep(1)
        continue
    elif key == "p": #resetting the highscore
        high = 0
        save_highscore(0)
        print("HIGH SCORE RESET")
        print()
        continue
    if check_game_over(board): #checking for game over if the board gets filled with no merges possible
        print("************2048************")
        print()
        print_board(board)
        print()
        print("GAME OVER")
        print(f"Final Score: {score}   Final Moves: {moves}   High: {high}")
        print("*" * w)
        print()
        break
