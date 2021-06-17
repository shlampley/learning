from itertools import cycle
class Players:
    def __init__(self, name, solo, multi):
        self.name = input("name")
        self.solo = solo
        
class Board:
    def __init__(self):
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
    def get_player_iterator(self):
        return cycle(self.turns)
class Game:
    def __init__(self, win = [], tie = []):
        self.win = win
        self.tie = tie
        self.winner = ""

    def game_loop(self):
        # We need to make a new board        
        x1 = Board()
        # We need to display the current board state
        # we need to get the users choice of where to place their move
        for x in x1.moves:
            x1 = user_inputs(x1) # need to store value!!!!!!!!!!!!!!!!!!!!!!!!!!
            # if self.check_win(x1):
            if self.check_win(x1):
                print(x1)
                print(f"Player {self.winner} Won")
                break
        # repeat until????
        # print final game state
        self.win.append(x1)
        return x1
        # while True:
        #     if x1 == win_board:
        #         print(f"{next} YOU WIN!!!! ")
        #     else:
        #         print(f"{next} YOU WIN!!!! ")
    def check_win(self, board):
        # Check diagonal
            # Check for X
            if board.moves[0] == "X" and board.moves[4] == "X" and board.moves[8] == "X":
                self.winner = "X"
                return True
            elif board.moves[2] == "X" and board.moves[4] == "X" and board.moves[6] == "X":
                self.winner = "X"
                return True      
            # Check for O
            elif board.moves[0] == "O" and board.moves[4] == "O" and board.moves[8] == "O":
                self.winner = "O"
                return True
            elif board.moves[2] == "O" and board.moves[4] == "O" and board.moves[6] == "O":
                self.winner = "O"
                return True
            # Check Horizontals (3)
                # Check for X
            elif board.moves[0] == "X" and board.moves[1] == "X" and board.moves[2] == "X":
                self.winner = "X"
                return True            
            elif board.moves[3] == "X" and board.moves[4] == "X" and board.moves[5] == "X":
                self.winner = "X"
                return True
            elif board.moves[6] == "X" and board.moves[7] == "X" and board.moves[8] == "X":
                self.winner = "X"
                return True
                # Check for O
            elif board.moves[0] == "O" and board.moves[1] == "O" and board.moves[2] == "O":
                self.winner = "O"
                return True
            elif board.moves[3] == "O" and board.moves[4] == "O" and board.moves[5] == "O":
                self.winner = "O"
                return True
            elif board.moves[6] == "O" and board.moves[7] == "O" and board.moves[8] == "O":
                self.winner = "O"
                return True
        # Check Verticals (3)
            # Check for X
            elif board.moves[0] == "X" and board.moves[3] == "X" and board.moves[6] == "X":
                self.winner = "X"
                return True
            elif board.moves[1] == "X" and board.moves[4] == "X" and board.moves[7] == "X":
                self.winner = "X"
                return True
            elif board.moves[2] == "X" and board.moves[5] == "X" and board.moves[8] == "X":
                self.winner = "X"
                return True
            # Check for O
            elif board.moves[0] == "O" and board.moves[3] == "O" and board.moves[6] == "O":
                self.winner = "O"
                return True
            elif board.moves[1] == "O" and board.moves[4] == "O" and board.moves[7] == "O":
                self.winner = "O"
                return True
            elif board.moves[2] == "O" and board.moves[5] == "O" and board.moves[8] == "O":
                self.winner = "O"
                return True
            else:
                return False
def user_inputs(board):
    print("board object:")
    print(board)
    curr_turn = next(board.player_turn)
    #Move the line below me into the main game loop and instead
    choice = "10"
    while True:
        try:
            if int(choice) in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                print("got a valid input")
                board.moves[int(choice)] = curr_turn
                break    
            choice = input(f"{curr_turn} where do you want to move 0-8: ")
        except:
            choice = "10"
            print("Invalid Input! Please try again")
        
    return board # returns board with curent player selection     
game = Game()
win = game.game_loop()
