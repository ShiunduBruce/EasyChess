class Figures():
    def __init__(self, direction, x, y):
        self.direction = direction

    def movement(self, x, y):
        pass


"""
S is for Straight Line 
D is for Diagonal Line 
L is for L form line 
SorD is for Straight or Diagonal
"""


class Rook(Figures):
    def __init__(self, x, y):
        Figures.__init__(self, "S", x, y)


class Knight(Figures):
    def __init__(self, x, y):
        Figures.__init__(self, "L", x, y)


class Bishop(Figures):
    def __init__(self, x, y):
        Figures.__init__(self, "D", x, y)


class Pawn(Figures):
    def __init__(self, x, y):
        Figures.__init__(self, 'SorD', x, y)

