"""
game_logic.py
--------------
implements game logic
- adding random tiles
- sliding and merging rows
- rotating the board for directional movement
- performing left/up/right/down moves
- checking for game-over state

"""

import random
#fn used to add random tile to the board. it adds 2 with 90% chance else adds 4 to an empty location(contains 0)
def add_random_tile(board):
    pos= []
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                pos.append((r,c))   
    if not pos:
        return
    row,col = random.choice(pos)
    temp = random.randint(1,10)
    if(temp==10):
        board[row][col]=4
    else:
        board[row][col]=2

#it moves all non empty tiles to left and moves empty tiles to right
# eg. 2 0 0 4 => 2 4 0 0
def slide(row):
    new = []
    for v in row:
        if v != 0:
            new.append(v)
    for i in range(4 - len(new)):
        new.append(0)
    return new


#it merges two tiles of same value by doubling the one on left and making the other one empty atmost one time each move
# eg. 2 2 4 0 => 4 0 4 0
def merge(row):
    for i in range(3):
        if row[i]==row[i+1] and row[i]!=0:
            row[i]*=2
            row[i+1]=0
    return row

#it moves the board left by first sliding all rows, merging tiles and again sliding them 
# eg. 2 2 0 4 => 2 2 4 0 => 4 0 4 0 => 4 4 0 0
def move_left(board):
    result = []
    for row in board:
        row = slide(row)
        row = merge(row)
        row = slide(row)
        result.append(row)
    return result

#it rotates board 90 degrees clockwise, used for the next function
def rotate(board):
    new = [[0]*4 for i in range(4)]
    for r in range(4):
        for c in range(4):
            new[c][3-r] = board[r][c]
    return new

#as the code only moves board to the left we can use rotate to reuse the code for the other directions because it is easier than writing each separately
# eg. to move board down, first rotate 90 degrees clockwise, move board left, rotate 270 degrees clockwise
def move_board(board, key):
    keys = {"a":0,"s":1,"d":2,"w":3}
    d = keys[key]
    cpy = [r[:] for r in board]
    for i in range(d):
        cpy = rotate(cpy)
    new = move_left(cpy)
    if d == 0: rng = 0
    else: rng = 4-d
    for j in range(rng):
        new = rotate(new)
    moved = (new != board) #if new is different from board it means board has actually moved
    #that is useful because we are not supposed to add new tile if the board hasn't moved 
    gain = 0        #score added after this move
    for r in range(4):
        for c in range(4):
            if new[r][c] > board[r][c]:
                gain += new[r][c] - board[r][c]
    if moved:       #if moved then copy new board into original one
        for r in range(4):
            board[r] = new[r][:] 
    return moved, gain

#fn checks if game is over. if there is an empty cell, game not over. else if board is full and no mergeable tiles, then game-over
def check_game_over(board):
    if any(0 in row for row in board):
        return False
    for r in range(4):
        for c in range(4):
            if r < 3 and board[r][c] == board[r+1][c]:
                return False
            if c < 3 and board[r][c] == board[r][c+1]:
                return False
    return True
