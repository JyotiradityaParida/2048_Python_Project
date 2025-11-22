"""
board.py
---------
contains functions for creating the 4x4 board and printing it in a formatted
grid layout.

"""

#this fn makes a board (a matrix filled with 0s)
def create_board():
    lis = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(0)
        lis.append(temp)
    return lis

#this fn is used to print the board. if element is 0, print blank, else print the number after alignment
def print_board(board):
    print("+------"*4+"+")
    for row in board:
        for v in row:
            if v == 0:
                print("|      ", end="")
            else:
                print(f"|{v:^6}", end="")
        print("|")
        print("+------"*4+"+")
