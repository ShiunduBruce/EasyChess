# from tkinter.constants import FALSE
# from PIL import Image, ImageTk
# import os

class Figure():

    def __init__(self, piece, color):
        self.piece = piece
        self.color = color
        result = piece[0] if color == "white" else piece[0].upper()
        self.abbriviation = color = result
        self.in_board = False

    def is_inside_border(self, coords):
        result = coords[0] >= 1 and coords[0] <= 4
        return result and coords[1] >= 0 and coords[1] <= 3

    def get(self, idx, board):
        return board.field[idx[0]][idx[1]]

    def __str__(self):
        return self.abbriviation

    def check_move_possible(self, position, target, board):
        if self.in_board:
            orthogonal = ((-1, 0), (0, -1), (0, 1), (1, 0))
            diagonal = ((-1, -1), (1, 1), (1, -1), (-1, 1))

            if self.abbriviation == 'r' or self.abbriviation == 'R':
                move = orthogonal

            if self.abbriviation == 'b' or self.abbriviation == 'B':
                move = diagonal

            for x, y in move:
                collision = False

                # Iteration position
                curr_pos = position[0] + x, position[1] + y

                # Board size 4x4, checking if indexes are always inside board
                while not collision and self.is_inside_border(curr_pos):

                    # Checking if we reached the target
                    if curr_pos == target:
                        a = self.get(target, board) == 0
                        b = self.get(position, board).color
                        if a or b != self.get(target, board).color:
                            return True
                        return False
                    
                    # Checking if there is collision in between
                    if(self.get(curr_pos, board) != 0):
                        collision = True
                    
                    curr_pos = curr_pos[0] + x, curr_pos[1] + y
            
            # Reaching that target is either not allowed or there is collision
            return False

        if not self.is_inside_border(target):
            return False

        self.in_board = True
        return True


class Knight(Figure):
    def __init__(self, color):
        Figure.__init__(self, "knight", color)

    def check_move_possible(self, position, target, board):
        if self.in_board:
            l_move = ((1, 2), (2, -1), (-1, -2), 
                        (-2, 1), (-1, 2), (2, 1), (1, -2), (-2, -1))

            for x, y in l_move:
                # Iteration position
                curr_pos = position[0] + x, position[1] + y

                # Board size 4x4, checking if indexes are always inside board
                if self.is_inside_border(curr_pos) and curr_pos == target:
                    a = self.get(target, board) == 0
                    b = self.get(position, board).color
                    if a or b != self.get(target, board).color:
                        return True
                    return False
            
            # Reaching that target is either not allowed or there is collision
            return False

        if not self.is_inside_border(target):
            return False

        self.in_board = True
        return True


class Pawn(Figure):
    def __init__(self, color):
        Figure.__init__(self, "pawn", color)
        self.is_reverse = False

    def check_reverse(self, idx):
        if idx == 4:
            self.is_reverse = False
        
        if idx == 1:
            self.is_reverse = True

    def check_move_possible(self, position, target, board):
        a = (1 if self.is_reverse else -1, 0)
        b = (1 if self.is_reverse else -1, -1)
        c = (1 if self.is_reverse else -1, 1)
        move = (a, b, c)

        if self.in_board:
            curr_pos = position[0] + move[0][0], position[1] + move[0][1] 

            if self.is_inside_border(curr_pos) and curr_pos == target:
                if self.get(target, board) == 0:
                    self.check_reverse(target[0])
                    return True
                return False

            for i in (1, 2):
                curr_pos = position[0] + move[i][0], position[1] + move[i][1]

                if self.is_inside_border(curr_pos) and curr_pos == target:
                    a = self.get(target, board) != 0
                    b = self.get(position, board).color
                    if a and b != self.get(target, board).color:
                        self.check_reverse(target[0])
                        return True
                    return False
            
            # Reaching that target is either not allowed or there is collision
            return False

        if not self.is_inside_border(target):
            return False

        self.in_board = True
        self.check_reverse(target[0])
        return True


class Rook(Figure):
    def __init__(self, color):
        Figure.__init__(self, "rook", color)      


class Bishop(Figure):
    def __init__(self, color):
        Figure.__init__(self, "bishop", color)
