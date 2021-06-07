class Players:
    def __init__(self, name, solo, multi):
        self.name = input("name")
        self.solo = solo
        
class Board:
    def __init__(self):
        self.board = ""    
    def __str__(self):
        return "this is a board object"
    def __repr__(self):
        return "this is a board object"    
    
    def draw(self):
        for x in range(-1, 6):
            if x % 2 == 0:
                self.board += '|      ' * 4
                self.board += '\n|  1   |  2   |  3   |'
            else:
                self.board +=  ' ______' * 3
            self.board += '\n'
        return self.board
x1 = Board()
x1.draw()
class BoardTile(Board):
    def __init__(self, player_marker, coordinates):
        self.player_marker = player_marker
        self.coordinates = coordinates
        for x in range(-1, 6):
            #input("Choose move")
            break
    
    print(x1.board)

movelist =[]
movelist.append(BoardTile("O","B2"))