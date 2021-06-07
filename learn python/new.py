game_board = ""
def draw():
    board = ""
    for x in range(-1, 6):
        if x % 2 == 0:
            board += '|      ' * 4
            board += '\n|  1   |  2   |  3   |'
        else:
            board +=  ' ______' * 3
        board += '\n'
    return board
draw()
