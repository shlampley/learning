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
# NEVER USED 
game_board = ""

def draw():
    game_board = ""
    for x in range(-1, 2):
        if x % 2 == 0:
            game_board += f' ____________________\n|      |      |      |\n|  {x}   |  {x+1}   |  {x+2}   |\n|______|______|______|\n|      |      |      |\n|  {x+3}   |  {x+4}   |  {x+5}   |\n|______|______|______|\n|      |      |      |\n|  {x+6}   |  {x+7}   |  {x+8}   |\n|______|______|______|'
    print(game_board)
draw()

# def print_game_state(move_array):
#     # Define header letters:
#     header_letters = ["A", "B", "C"]
#     # We order the list
#     ordered_moves = order_moves(move_array)
#     # We fill any gaps with #
#     filled_moves = fill_gaps(ordered_moves)
#     # convert into a 2d array with only move values:
#     grid_moves = gridify_moves(filled_moves)
#     print("  ", end="")
#     for i in range(0,3):
#         print(i+1, end="")
#     print("")

# TODO: \/Focus on this section for solution
#     for i in range(0,3):
#         print(header_letters[i], end="")
#         print(" ", end="")
#         for j in range(0,3):
#             print(grid_moves[i][j].grid_value, end="")
#         print("")
# Result is : 
#   1 2 3
# A X # #
# B # O #
# C # # #

# loop 1 loop through x coord from 0 to 3
#     loop 2 loop through y coord from 0 to 3



#     x->
#     ______ ______ ______
# y   |      |      |      |
# |   |  0,0 |  1,0 |  2,0 |
#     ______ ______ ______
#     |      |      |      |
#     |  1,0 |  1,1 |  2,1 |
#     ______ ______ ______
#     |      |      |      |
#     |  1   |  2   |  3   |
#     ______ ______ ______