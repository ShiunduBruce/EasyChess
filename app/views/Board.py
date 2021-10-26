import tkinter
class Board():
    def __init__(self, figures):
        self.STARTING = "rbkp-RBKP"
        self.field = []
        self.reset (figures)
        
    def print_board (self):
        for i in range (1, len(self.field)-1):
            print ([str (self.field[i][j]) for j in range (len(self.field[i]))], sep=", ")
    
    def reset (self, figures):
        self.field = [[figures[0],figures[1],figures[2],figures[3]],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [figures[4],figures[5],figures[6],figures[7]]]

    def get_default_coords (self, letter):
        if str.islower(letter):
            return 0, self.STARTING.index(letter)
        
        return 5, self.STARTING.index(letter) - 5



"""
Board
R, B, N, P - for White pieces
r, b, n, p - for Black pieces

r - rook
b - bishop
n - knight
p - pawn

"""