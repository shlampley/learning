# from typing import Iterable


# board = [["|   |" for a in range(3) + "\n"] for b in range(3)]
# print(board)

# # Lookup map() function for defining the board

# # https://www.geeksforgeeks.org/python-map-function/
# # map(boardNEwline,iterables=)

# def boardNEwline():
#     pass
#     # return how to tell it where to add the newline
#     # OOP object oriented programming vs functional and linear


#from programs.testing2 import print_board
# 

#from programs.tic_tac_toe import Board


# not functioning correctly, in my tiv-tac-toe board it prints normal but here it dosnt
game_board = ""
def draw():
    game_board = []
    board = game_board
    for x in range(-1, 6):
        if x % 2 == 0:
            board += '|      ' * 4
            board += '\n|  1   |  2   |  3   |'
        else:
            board +=  ' ______' * 3
        board += '\n'
    print(game_board)
draw()

