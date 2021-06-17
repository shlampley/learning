from TicTac import TicTac
from itertools import cycle
import os

def get_coordinates(player):
    # We put a loop here to ensure valid input before continuing on:
    valid = False
    while not valid:
        coords = input(f"Please input the coordinate you would like to set {player}: ")
        temp = verify_input(coords)
        if coords in "Dd":
            break
        if temp == "":
            valid = True
        else:
            print(temp)
    return coords

# Even though we programed the class to have exceptions raised if invalid things are put into the class the program crashes out, so we can handle this in two ways,
# Catch the exception and handle it based on the output or stop it from ever raising the exception by calidating before putting it into the class
def verify_input(user_input):
    # First we split the input into two parts 
        user_message = ""
        grid_vals = list(user_input)
        grid_x = grid_vals[0]
        if grid_x in "Dd":
            return ""
        grid_y = grid_vals[1]
        # We verify that the first coordinate is in the valid range
        if grid_x not in "ABCabc":
            user_message += f" {grid_x} is out of range (A-C);"
        # We verify that the second coordinate is within range
        if int(grid_y) > 3:
            user_message += f" {grid_y} is out of range, too large; should be between (1 and 3) inclusive;"
        if int(grid_y) < 1:
            user_message += f" {grid_y} is out of range, too small; should be between (1 and 3) inclusive;"
        return user_message

def game_loop():
    coords = ""
    players = ["X", "O"]
    moves = []
    temp_move = [TicTac("A1", "#")]
    # creates an iterator that toggles between the two Player turns, would support more than two
    player_iterator = cycle(players)
    while True:
        # Clear terminal
        clear()
        if not moves:
            print_game_state(temp_move)
        else:
            print_game_state(moves)
        player = next(player_iterator)
        coords = get_coordinates(player)
        # print(f"THe current Player is {player}")
        # print(f"The current Coords is {coords}A")
        if coords in "Dd":
            break
        tempTurn = TicTac(str(coords),str(player))
        moves.append(tempTurn)
    return moves

def order_moves(moves_array):
    ordered_moves = sorted(moves_array, key=lambda moves: moves.grid_location)
    return ordered_moves

# Now we have a list of game moves and the positions lets make it into a nice ordered list so we can display the game board 
def gridify_moves(moves_array):
    # create an iterator for ease of use and less loops
    moves_iterator = iter(moves_array)
    # now we turn it into a double array:
    coordified = [[0]*3 for _ in range(3)]
    for i in range(0,3):
        for j in range(0,3):
            coordified[i][j] = next(moves_iterator)
    return coordified

def fill_gaps(move_array):
    # First we generate an empty list of the general coordinates
    temp_coords = []
    temp_coords += [f"A{i}" for i in range(1,4)]
    temp_coords += [f"B{i}" for i in range(1,4)]
    temp_coords += [f"C{i}" for i in range(1,4)]
    # here we use zip to traverse both arrays simultaneously Now we are moving to use iterators for more flexibility
    move_iterator = iter(move_array)
    # Keep track of the number of iterations in the loop
    i = 0
    for coords in temp_coords:
        # We check if the array has reached the end and if it has we fill it up
        if len(move_array) <= i:
            temp_move = TicTac(coords,"#")
            move_array.append(temp_move)
        elif move_array[i].grid_location != coords:
        # We found a gap that needs to be filled with a placeholder to draw the grid.
            temp_move = TicTac(coords,"#")
            move_array.insert(i, temp_move)
        # Now we iterate
        i += 1
        
    return move_array
    
def print_game_state(move_array):
    # Define header letters:
    header_letters = ["A", "B", "C"]
    # We order the list
    ordered_moves = order_moves(move_array)
    # We fill any gaps with #
    filled_moves = fill_gaps(ordered_moves)
    # convert into a 2d array with only move values:
    grid_moves = gridify_moves(filled_moves)
    print("  ", end="")
    for i in range(0,3):
        print(i+1, end="")
    print("")
    for i in range(0,3):
        print(header_letters[i], end="")
        print(" ", end="")
        for j in range(0,3):
            print(grid_moves[i][j].grid_value, end="")
        print("")
def clear():
    os.system("cls")

def main():
    game_moves = game_loop()
    print_game_state(game_moves)

if __name__ == "__main__":
    main()