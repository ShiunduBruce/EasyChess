class Figure():
    ##__slots__ = ('abbriviation', 'color')

    def __init__(self, abbriviation, color):
        self.abbriviation = abbriviation

        if color == 'white':
            self.abbriviation = self.abbriviation.upper()
        elif color == 'black':
            self.abbriviation = self.abbriviation.lower()

        self.color = color

    def possible_moves(self, position, orthogonal, diagonal, distance):
        pass

    def __str__(self):
        return self.abbriviation




class Knight(Figure):
    def __init__(self, color):
        Figure.__init__(self, "k", color)

class Pawn(Figure):
    def __init__(self, color):
        Figure.__init__(self, "p", color)

class Rook(Figure):
    def __init__(self, color):
        Figure.__init__(self, "r", color)

class Bishop(Figure):
    def __init__(self, color):
        Figure.__init__(self, "b", color)

"""
S is for Straight Line 
D is for Diagonal Line 
L is for L form line 
SorD is for Straight or Diagonal
"""


