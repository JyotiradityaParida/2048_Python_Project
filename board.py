def create_board():
    lis = []
    for i in range(4):
        temp = []
        for j in range(4):
            temp.append(0)
        lis.append(temp)
    return lis

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