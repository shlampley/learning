from itertools import cycle
import os

class Player:
    def __init__(self, name):
        self.name = name
    
    def move(self, callback):
        callback(self.name)
        pass
        # TODO call game logic for non-bot to take a turn AKA getting input
        
    
class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
    # CREATE BOT LOGIC


class Board:
    def __init__(self):
        self.board = ""
        self.moves = self.set_empty_moves()
        

        # self.win_board() = ########################
    def __str__(self):
        return self.get_board()
    def __repr__(self):
        return "this is a board object"    
    
    def set_empty_moves(self):
        temp_list = []
        temp_list.append("0️⃣")
        temp_list.append("1️⃣")
        temp_list.append("2️⃣")
        temp_list.append("3️⃣")
        temp_list.append("4️⃣")
        temp_list.append("5️⃣")
        temp_list.append("6️⃣")
        temp_list.append("7️⃣")
        temp_list.append("8️⃣")
        return temp_list
 
    def get_board(self):
        
        self.board = f' ____________________\n|      |      |      |\n|  {self.moves[0]}   |  {self.moves[1]}   |  {self.moves[2]}   |\n|______|______|______|\n|      |      |      |\n|  {self.moves[3]}   |  {self.moves[4]}   |  {self.moves[5]}   |\n|______|______|______|\n|      |      |      |\n|  {self.moves[6]}   |  {self.moves[7]}   |  {self.moves[8]}   |\n|______|______|______|'
        return self.board
    
class Game:
    def __init__(self, win = [], tie = []):
        self.turns = ["⛌", "◯"] # TODO see line 61        
        self.players = self.set_players()
        self.quitting_chars = ["Q","quit"]
        self.win = win
        self.tie = tie
        self.winner = ""
        self.quit = True
        self.board = Board()
        self.player_turn = self.get_player_iterator()
    def get_player_iterator(self):
        # TODO:Create an array with an X player and an O player with the names of turns[0] and turns[1]
        return cycle(self.players)
    def set_players(self):
        # TODO: finish writing this to return the player array
        player_1 = Player(self.turns[0]) # need to designate name using turns[0]
        player_2 = Player(self.turns[1])# need to designate name using turns[1]
        return [player_1, player_2]    
    def check_taken(self, choice):
        if str(self.board.moves[int(choice)]) in self.turns:
            print("Position taken try another spot: ")
            return True
        else:
            return False    


    
    def user_inputs(self, player_marker):
        print(self.board)
        # Move the line below me into the main game loop and instead
        choice = "10"
        while True:
            try:
                quit_string = " or ".join([", ".join(self.quitting_chars[:-1]),self.quitting_chars[-1]])
                # quit_string = " or ".join(["Q, q",self.quitting_chars[-1]])
                # quit_string = " or ".join(["Q, q","exit"])
                # quit_string = "Q, q" + " or " + "exit"

                choice = input(f'{player_marker} where do you want to move 0-8 or {quit_string} to quit: ')
                if choice and choice in "0, 1, 2, 3, 4, 5, 6, 7, 8":  
                    if not self.check_taken(choice):               
                        self.board.moves[int(choice)] = player_marker
                        break
                elif choice and choice.upper() in self.quitting_chars:
                    self.end_game()
                else:
                    choice = "10"
                    print("Invalid Input! Please try again")
                

              
            except KeyboardInterrupt:
                self.end_game()
                
            # print(board)           
   

    def end_game(self):
        # print("")
        print("\nThanks for playing!")
        exit()
    
    def game_loop(self):
        # We need to make a new board        
        # We need to display the current board state
        # we need to get the users choice of where to place their move
        for x in self.board.moves:
            os.system("cls")
            next(self.player_turn).move(self.user_inputs)
            
            # if self.check_win(x1):
            if self.check_win():
                print(self.board)
                print(f"Player {self.winner} Won")
                break
        # repeat until????
        # print final game state
        self.win.append(self.board)
        return self.board

    def check_win(self):
        print("made it")
        board = self.board
        print(self.board)
        x_move = self.turns[0]
        o_move = self.turns[1]
        print(x_move)
        print(o_move)
        # Check diagonal
        # Check for X
        print(board.moves)
        if board.moves[0] == x_move and board.moves[4] == x_move and board.moves[8] == x_move:
            self.winner = x_move
            return True
        elif board.moves[2] == x_move and board.moves[4] == x_move and board.moves[6] == x_move:
            self.winner = x_move
            return True      
        # Check for O
        elif board.moves[0] == o_move and board.moves[4] == o_move and board.moves[8] == o_move:
            self.winner = o_move
            return True
        elif board.moves[2] == o_move and board.moves[4] == o_move and board.moves[6] == o_move:
            self.winner = o_move
            return True
        # Check Horizontals (3)
            # Check for X
        elif board.moves[0] == x_move and board.moves[1] == x_move and board.moves[2] == x_move:
            self.winner = x_move
            return True            
        elif board.moves[3] == x_move and board.moves[4] == x_move and board.moves[5] == x_move:
            self.winner = x_move
            return True
        elif board.moves[6] == x_move and board.moves[7] == x_move and board.moves[8] == x_move:
            self.winner = x_move
            return True
            # Check for O
        elif board.moves[0] == o_move and board.moves[1] == o_move and board.moves[2] == o_move:
            self.winner = o_move
            return True
        elif board.moves[3] == o_move and board.moves[4] == o_move and board.moves[5] == o_move:
            self.winner = o_move
            return True
        elif board.moves[6] == o_move and board.moves[7] == o_move and board.moves[8] == o_move:
            self.winner = o_move
            return True
        # Check Verticals (3)
        # Check for X
        elif board.moves[0] == x_move and board.moves[3] == x_move and board.moves[6] == x_move:
            self.winner = x_move
            return True
        elif board.moves[1] == x_move and board.moves[4] == x_move and board.moves[7] == x_move:
            self.winner = x_move
            return True
        elif board.moves[2] == x_move and board.moves[5] == x_move and board.moves[8] == x_move:
            self.winner = x_move
            return True
        # Check for O
        elif board.moves[0] == o_move and board.moves[3] == o_move and board.moves[6] == o_move:
            self.winner = o_move
            return True
        elif board.moves[1] == o_move and board.moves[4] == o_move and board.moves[7] == o_move:
            self.winner = o_move
            return True
        elif board.moves[2] == o_move and board.moves[5] == o_move and board.moves[8] == o_move:
            self.winner = o_move
            return True
        else:
            print("Draw: ")
            return False



game = Game()
win = game.game_loop()
