import random

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

def slide(row):
    new = []
    for v in row:
        if v != 0:
            new.append(v)
    for i in range(4 - len(new)):
        new.append(0)
    return new

def merge(row):
    for i in range(3):
        if row[i]==row[i+1] and row[i]!=0:
            row[i]*=2
            row[i+1]=0
    return row

def move_left(board):
    result = []
    for row in board:
        row = slide(row)
        row = merge(row)
        row = slide(row)
        result.append(row)
    return result

def rotate(board):
    new = [[0]*4 for i in range(4)]
    for r in range(4):
        for c in range(4):
            new[c][3-r] = board[r][c]
    return new

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
    moved = (new != board)
    gain = 0
    for r in range(4):
        for c in range(4):
            if new[r][c] > board[r][c]:
                gain += new[r][c] - board[r][c]
    if moved:
        for r in range(4):
            board[r] = new[r][:] 
    return moved, gain

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