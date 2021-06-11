from itertools import cycle

class Game():
    def __init__(self, win, tie):
        self.win = []
        self.tie = []

class Players:
    def __init__(self, name, solo, multi):
        self.name = input("name")
        self.solo = solo
        
class Board:
    def __init__(self):
        self.win_board = ""
        self.board = ""
        self.moves = self.set_empty_moves()
        self.turns = ["X", "O"]
        self.player_turn = self.get_player_iterator()
        # self.win_board() = ########################
    def __str__(self):
        return self.get_board()
    def __repr__(self):
        return "this is a board object"    
    
    def set_empty_moves(self):
        return [x for x in range(9)]
        
    def get_board(self):
        
        self.board = f' ____________________\n|      |      |      |\n|  {self.moves[0]}   |  {self.moves[1]}   |  {self.moves[2]}   |\n|______|______|______|\n|      |      |      |\n|  {self.moves[3]}   |  {self.moves[4]}   |  {self.moves[5]}   |\n|______|______|______|\n|      |      |      |\n|  {self.moves[6]}   |  {self.moves[7]}   |  {self.moves[8]}   |\n|______|______|______|'
        return self.board
    #def get_winnig_board(self):
    
    #def save_winnig_board(self):
    #  def get_base_board(self):
    #     x = 0
    #     return f' ____________________\n|      |      |      |\n|  {x}   |  {x+1}   |  {x+2}   |\n|______|______|______|\n|      |      |      |\n|  {x+3}   |  {x+4}   |  {x+5}   |\n|______|______|______|\n|      |      |      |\n|  {x+6}   |  {x+7}   |  {x+8}   |\n|______|______|______|'

    # Used to get the current turn
    def get_player_iterator(self):
        return cycle(self.turns)
    
    # def winner():   #####################
    #     x2 = Board()
    #     if x2 ==


# Rec
def user_inputs(board):
    curr_turn = next(board.player_turn)
    #Move the line below me into the main game loop and instead
    print(board)
    choice = input(f"{curr_turn} where do you want to move 0-8: ")
    board.moves[int(choice)] = curr_turn
    return board # returns board with curent player selection


def game():
    # We need to make a new board
    win_board = ""
    x1 = Board()
    # We need to display the current board state
    # we need to get the users choice of where to place their move
    for x in x1.moves:
        x1 = user_inputs(x1) # need to store value!!!!!!!!!!!!!!!!!!!!!!!!!!
    # repeat until????
    # print final game state
    return win_board
    # while True:
    #     if x1 == win_board:
    #         print(f"{next} YOU WIN!!!! ")
    #     else:
    #         print(f"{next} YOU WIN!!!! ")

    

    



game()

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
