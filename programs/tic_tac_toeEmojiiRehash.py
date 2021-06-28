from itertools import cycle
import os
import math
import GameUtil as GU


class Player:
    def __init__(self, name):
        self.name = name
    
    def move(self, quit_string, board):
        return input(f'{self.name} where do you want to move 0-8 or {quit_string} to quit: ')
    # TODO call game logic for non-bot to take a turn AKA getting input

class Bot(Player):
    def __init__(self, name):
        super().__init__(name)
        self.scores = self._set_scores()
        
    def _set_scores(self):
        return {
            GU.turns[0]: 1,
            GU.turns[1]: -1,
            "Draw": 0
        }


    def move(self, quit_string, board):
        bestScore = -math.inf
        score = 0
        for i, move in enumerate(board.moves):
            # Is the spot available?
            if not GU.is_taken(move): 
                tmp_move = board.moves[i]
                board.moves[i] = GU.turns[1]
                score = self.min_max(board, 0, False)
                board.moves[i] = tmp_move
            elif score > bestScore:
                bestScore = score
                temp_move = i 
        return i

    def min_max(self, board, depth, is_maximizing):
        print(depth)
        # check if we have a winner
        result = GU.check_winner(board)
        # Check that there is a win condition 
        if result != None:
            return self.scores[result]
        

        if is_maximizing:
            best_score = -math.inf
            for i, move in enumerate(board.moves):
                if not GU.is_taken(move):
                    if int(depth) < 5:
                        temp = board.moves[i]
                        board.moves[i] = GU.turns[1]
                        score = self.min_max(board, depth+1, False)
                        board.moves[i] = temp
                        best_score = max(score, best_score)
                    else:
                        return max
            return best_score
        else:
            best_score = math.inf
            for i, move in enumerate(board.moves):
                if not GU.is_taken(move):
                    temp = board.moves[i]
                    board.moves[i] = GU.turns[0]
                    score = self.min_max(board, depth+1, True)
                    board.moves[i] = temp
                    best_score = min(score, best_score)

            return best_score

class Game:
    def __init__(self):
        self.players = self.set_players()
        self.winner = ""
        self.quit = True
        self.board = Board()
        self.player_turn = self.get_player_iterator()
        self.current_player = None

    def get_player_iterator(self):
        # TODO:Create an array with an X player and an O player with the names of turns[0] and turns[1]
        return cycle(self.players)

    def set_players(self):
        # TODO: finish writing this to return the player array
        player_1 = Player(GU.turns[0]) # need to designate name using turns[0]
        player_2 = Bot(GU.turns[1])# need to designate name using turns[1]
        return [player_1, player_2]

    def end_game(self):
        # print("")
        print(self.board)
        print("\nThanks for playing!")
        exit()
    
    def move_player(self):
        print(self.board)
        # Move the line below me into the main game loop and instead
        choice = "10"
        while True:
            try:
                choice = str(self.current_player.move(GU.quit_string, self.board))
                if choice and choice in "0, 1, 2, 3, 4, 5, 6, 7, 8":  
                    if not GU.check_taken(choice, self.board):               
                        self.board.moves[int(choice)] = self.current_player.name
                        break
                elif choice and choice.upper() in GU.quitting_chars:
                    self.end_game()
                else:
                    choice = "10"
                    print("Invalid Input! Please try again")
                

              
            except KeyboardInterrupt:
                self.end_game()
                
            # print(board)  
            
    def game_loop(self):
        # We need to make a new board        
        # We need to display the current board state
        # we need to get the users choice of where to place their move
        for x in self.board.moves:
            os.system("cls")
            print(self.board)
            #get current Player
            # player = next(self.player_turn)
            # #get current players name
            # player_name = player.name
            # player_move = player.move(GU.quit_string, self.board)
            # if player_move in GU.quitting_chars:
            #     self.end_game()
            # else:
            #     player_move = int(player_move) 
            # self.board.moves[player_move] = player_name
            # Advance player turn
            self.current_player = next(self.player_turn)
            # Move the player 
            self.move_player()
            
            # if self.check_win(x1):
            if GU.check_won(self.board):
                print(self.board)
                print(f"Player {GU.check_winner()} Won")
                break
        # repeat until????
        # print final game state
        return self.board

     
# class Player:
#     def __init__(self, name):
#         self.name = name
    
#     def move(self, callback):
#         callback(self.name)
#         pass
#         # TODO call game logic for non-bot to take a turn AKA getting input
        
    
# class Bot(Player):
#     def __init__(self, name):
#         super().__init__(name)
#     # CREATE BOT LOGIC


class Board:
    def __init__(self):
        self.board = ""
        self.moves = self.set_empty_moves()
        

        # self.win_board() = ########################
    def __str__(self):
        return self.get_board()
    def __repr__(self):
        return "this is a board object"    
    def __iter__(self):
        return iter(self.moves)

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
 



game = Game()
win = game.game_loop()
