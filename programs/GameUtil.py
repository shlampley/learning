
def check_taken(choice, board):
    if str(board.moves[int(choice)]) in turns:
        print("Position taken try another spot: ")
        return True
    else:
        return False

def _create_quit_string():
    return " or ".join([", ".join(quitting_chars[:-1]),quitting_chars[-1]])
            # quit_string = " or ".join(["Q, q",quitting_chars[-1]])
            # quit_string = " or ".join(["Q, q","exit"])
            # quit_string = "Q, q" + " or " + "exit"



# Given three moves we check if they are all equal valid moves
def check_equal(a, b, c):
    return is_taken(a) and a == b and b == c 

# given a board marker determine if it is a player move or not
def is_taken(move):
    temp_bool = False
    if move in turns:
        temp_bool = True
    return temp_bool

# Given a fancy move marker turn it into its alphanumeric value
def parse_move(move):
    if move == turns[0]:
        return alpha_turns[0]
    if move == turns[1]:
        return alpha_turns[1]
    
def check_full(board):
    for move in board.moves:
        if move not in turns:
            return False
    return True

def check_winner(board):
    winner = None
    # Check diagonal
    
    if check_equal(board.moves[0], board.moves[4], board.moves[8]):
        winner = board.moves[0]
    elif check_equal(board.moves[2], board.moves[4], board.moves[6]):
        winner = board.moves[2]      
    # Check Horizontals (3)
        # Check for X
    elif check_equal(board.moves[0], board.moves[1], board.moves[2]):
        winner = board.moves[0]          
    elif check_equal(board.moves[3], board.moves[4], board.moves[5]):
        winner = board.moves[3]
    elif check_equal(board.moves[6], board.moves[7], board.moves[8]):
        winner = board.moves[6]
    # Check Verticals (3)
    elif check_equal(board.moves[0], board.moves[3], board.moves[6]):
        winner = board.moves[0]
    elif check_equal(board.moves[1], board.moves[4], board.moves[7]):
        winner = board.moves[1]
    elif check_equal(board.moves[2], board.moves[5], board.moves[8]):
        winner = board.moves[2]
    elif check_full(board):
            winner = "Draw"
    else:
        winner = None
    return winner

# rename to check won
def check_won(board):
    # is this a winning board
    if check_winner(board) in turns:
        return True
    else:
        return False

turns = ["⛌", "◯"] # TODO see line 61    
alpha_turns = ["X", "O"]    
quitting_chars = ["Q","quit"]
quit_string = _create_quit_string()
