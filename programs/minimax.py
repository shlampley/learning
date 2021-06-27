import random
from tic_tac_toeEmojii import Game
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
        x_score = 1
        o_score = -1
        tie = 0
    def best_move(self,depth, is_maximizing, choice ):
        best_score = -math.inf
        if self.check_win():
            return self.x_score
            score = minimax(self.board)
            if score > best_score:
                best_move = self.current_move


    # CREATE BOT LOGIC
    # def move(self, quit_string, board):
    #     # TODO: Write bot logic for taking a move here
    #     ran_num = random.randint(0,8)
    #     return ran_num