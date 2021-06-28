import random
from tic_tac_toeEmojiiRehash import Game
import math

class Player:
    def __init__(self, name):
        self.name = name
    
    def move(self, quit_string, board):
        return input(f'{self.name} where do you want to move 0-8 or {quit_string} to quit: ')
    # TODO call game logic for non-bot to take a turn AKA getting input


class Bot(Player, Game):
    def __init__(self, name):
        super().__init__(name)
        self.scores = _set_scores()
        
    def _set_scores(self):
        return
        {
            self.turns[0]: 1,
            self.turns[1]: -1,
            "Draw": 0
        }
    def best_move(self,depth, is_maximizing, choice ):
        best_score = -math.inf
        if self.check_win():
            return self.x_score
            score = minimax(self.board)
            if score > best_score:
                best_move = self.current_move

    def move(self, quit_string, board):
        bestScore = -math.inf
        for i, move in enumerate(board):
            # Is the spot available?
            if board[i] != self.is_taken(move): 
                tmp_move = board[i]
                board[i] = self.turns[1]
                score = self.min_max(board, 0, False)
                board[i] = tmp_move
            elif score > bestScore:
                bestScore = score
                move = i 
        board[i] = self.turns[1]

    def min_max(self, board, depth, is_maximizing):
        # check if we have a winner
        result = self.check_winner(board)
        # Check that there is a win condition 
        if result != None:
            return self.scores[result]
        

        if is_maximizing:
            best_score = -math.inf
            for i, move in enumerate(board):
                if not self.is_taken(move):
                    temp = board[i]
                    board[i] = self.turns[1]
                    score = self.min_max(board, depth+1, False)
                    board[i] = temp
                    best_score = max(score, best_score)



            return best_score
        else:
            best_score = math.inf
            for i, move in enumerate(board):
                if not self.is_taken(move):
                    temp = board[i]
                    board[i] = self.turns[0]
                    score = self.min_max(board, depth+1, True)
                    board[i] = temp
                    best_score = min(score, best_score)



            return best_score      
        

    # CREATE BOT LOGIC
    # def move(self, quit_string, board):
    #     # TODO: Write bot logic for taking a move here
    #     ran_num = random.randint(0,8)
    #     return ran_num