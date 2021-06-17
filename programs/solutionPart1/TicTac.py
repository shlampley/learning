
class TicTacException(Exception):
    """Base Tic Tac Exception class"""
    def __init__(self, value, message="A Tic Tac Exception has occurred"):
        self.message = message
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message

class TicTacInvalidRange(TicTacException):
    """Raised when either the x or y is an acceptable grid range value"""
    def __init__(self,grid_location,message="The Coordinate Values are invalid"):
        self.grid_locs = list(grid_location)
        self.grid_x = self.grid_locs[0]
        self.grid_y = self.grid_locs[1]
        self.message = message + f"You put {self.grid_x}, and {self.grid_y}"
    def checkwhich(self):
        if not self.grid_x.isalpha():
            self.message += f"{self.grid_x} is invalid; should be A, B or C"
        if not self.grid_y.isnumeric():
            self.message += f"{self.grid_x} is invalid; should be a number"
    def __repr__(self):
        return self.message
    def __str__(self):
        return self.message

class TicTacOutOfRange(TicTacException):
    """Raised when either the x or y is out of the acceptable grid range"""
    def __init__(self,grid_value,message="The Coordinate Values are out of range (A-C) and (1-3);"):
        self.grid_vals = list(grid_value)
        self.grid_x = self.grid_vals[0]
        self.grid_x = self.grid_x.upper()
        self.grid_y = self.grid_vals[1]
        self.message = message + f" You put {self.grid_x}, and {self.grid_y}; "
        self.checkwhich()
    def checkwhich(self):
        if self.grid_x not in "ABC":
            self.message += f" {self.grid_x} is out of range (A-C);"
        if int(self.grid_y) > 3:
            self.message += f" {self.grid_y} is out of range, too large; should be between (1 and 3) inclusive;"
        if int(self.grid_y) < 1:
            self.message += f" {self.grid_y} is out of range, too small; should be between (1 and 3) inclusive;"

class TicTacInvalidTurn(TicTacException):
    def __init__(self,value,message="Invalid Player Turn;"):
        self.valid_players = "XOx0#"
        self.value = value
        self.message = message
    def checkturn(self):
        self.message = self.message + f"You entered {self.value} which is invalid; The valid player turns are {self.valid_players}."
             
             
class TicTac:
    def __init__(self, grid_location="A1", grid_value="X", valid_players="XOxo"):
        self._grid_location = grid_location
        self._grid_value = grid_value
        self.grid_location = self._grid_location
        self.grid_value = self._grid_value
        self.valid_players = valid_players

    def __str__(self):
        return f"Grid Location: {self.grid_location}\nPlayer Marker: {self.grid_value}"
    def __repr__(self):
        return f"grid_location: {self.grid_location}\ngrid_value: {self.grid_value}"

    # Internal exception thrower for grid verification
    def verify_grid(self, grid_locs):
        grid = list(grid_locs)
        grid_x = grid[0]
        grid_x = grid_x.upper()
        grid_y = grid[1]
        if not grid_x.isalpha() or not grid_y.isnumeric():
            raise TicTacInvalidRange(grid_locs)
        elif str(grid_x) not in "ABC" or int(grid_y) > 3 or int(grid_y) < 1:
            raise TicTacOutOfRange(grid_locs)
            
    def verify_players(self, player):
        if player not in "XOxo#":
            raise TicTacInvalidTurn(player)

    @property
    def grid_location(self):
        return self._grid_location

    @grid_location.setter
    def grid_location(self, value):
        self.verify_grid(value)
        temp_array = list(value)
        rvalue = "Z0"
        if temp_array[0].isalpha() and temp_array[1].isnumeric():
            # Verify that the grid is within scope if not we raise an exception
            rvalue = ""
            rvalue = rvalue.join(temp_array)
        self._grid_location = rvalue.upper()

    @property
    def grid_value(self):
        return self._grid_value

    @grid_value.setter
    def grid_value(self, value):
        self.verify_players(value)
        if value.isalpha():
            self._grid_value = value.upper()


    # TODO set @property to make it so when we set the player value and the grid location they stay consistent
