import random
from tic_tac_toeEmojii import Game

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
    def best_move(self,depth, is_maximizing ):
        if self.check_taken():
            
        result = self.check_win()
        if result != True:
            score = ""
            score = score[result]
            return True
        if is_maximizing:






    # CREATE BOT LOGIC
    # def move(self, quit_string, board):
    #     # TODO: Write bot logic for taking a move here
    #     ran_num = random.randint(0,8)
    #     return ran_num