class Players:
    def __init__(self, name, solo, multi):
        self.name = input("name")
        self.solo = solo
        
class Board:
    def __init__(self):
        self.board = ""    
    def __str__(self):
        return self.get_board()
    def __repr__(self):
        return "this is a board object"    
    
    def get_board(self):
        x = 0
        self.board = f' ____________________\n|      |      |      |\n|  {x}   |  {x+1}   |  {x+2}   |\n|______|______|______|\n|      |      |      |\n|  {x+3}   |  {x+4}   |  {x+5}   |\n|______|______|______|\n|      |      |      |\n|  {x+6}   |  {x+7}   |  {x+8}   |\n|______|______|______|'
        return self.board
    def get_base_board(self):
        x = 0
        return f' ____________________\n|      |      |      |\n|  {x}   |  {x+1}   |  {x+2}   |\n|______|______|______|\n|      |      |      |\n|  {x+3}   |  {x+4}   |  {x+5}   |\n|______|______|______|\n|      |      |      |\n|  {x+6}   |  {x+7}   |  {x+8}   |\n|______|______|______|'
def user_inputs(x1.get_base_board):
    print(x1.get_base_board)
x1 = Board()
x1.get_board()
user_inputs(x1)
# class BoardTile(Board):
#     def __init__(self, player_marker, coordinates):
#         self.player_marker = player_marker
#         self.coordinates = coordinates
#         for x in range(-1, 6):
#             #input("Choose move")
#             break
    
#     print(x1.board)

# movelist =[]
# movelist.append(BoardTile("O","B2"))
