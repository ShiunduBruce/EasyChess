# UNCOMMENT THIS FOR LOCAL RUN
# import Board as Board
# import figures.Figure as Figure


# This works for CI, comment this when running locally
import app.views.Board as Board
import app.views.figures.Figure as Figure

import tkinter as tk
from PIL import Image, ImageTk
from images.ImageHelper import ImageHelper

import math

class BoardGuiTk(tk.Tk):
    rows = 4
    columns = 4

    color1 = "white"
    color2 = "gray"

    icons = {}
    pieces_canvas = {}

    id_target = None
    target_location = None
    clicked_item = None

    prev_coords = None
    curr_coords = None
    board_abbriviations = None

    def __init__(self, square_size=90):
        super().__init__()
        
        # Image data
        self.imageHelper = ImageHelper()

        # figures instances

        self.figures = [Figure.Rook("white"), Figure.Bishop("white"),
                            Figure.Knight("white"), Figure.Pawn("white"),
                                Figure.Rook("blue"), Figure.Bishop("blue"), 
                                Figure.Knight("blue"), Figure.Pawn("blue")]

        self.board = Board.Board(self.figures)

        self.square_size = square_size
        canvas_width = self.columns * square_size
        canvas_height = (self.rows * square_size) + square_size * 2

        self.player1Turn = True

        # configure the root window
        self.title('EasyChess App')
        # self.geometry('600x800')

        self.canvas = tk.Canvas(self, width=canvas_width, 
                            height=canvas_height, background="gray")
        self.canvas.pack(fill="both", expand=1)

        self.statusbar = tk.Frame(self, height=64)
        self.button_reset = tk.Button(self.statusbar, text="Reset", 
                                fg="black", command=self.reset)
        self.button_reset.pack(side=tk.LEFT, in_=self.statusbar)
        self.statusbar.pack(expand=False, fill="x", side='bottom')

        #  mouse events
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.move)
        self.canvas.bind("<ButtonRelease-1>", self.release)
        self.best_move = None
    def reset(self):
        self.board.reset(self.figures)

        for figure in self.figures:
            figure.in_board = False

        #self.undoMove (self.prev_coords, self.curr_coords, self.board_abbriviations)
        self.refresh()

    def refresh(self):
        # Draws items on the GUI depending on the board.field
        for i in range(0, self.rows + 2):
            for j in range(self.columns):
                if self.board.field[i][j] != 0:
                    coords = self.getCoords(i, j)
                    id_figure = self.get_id(self.board.field[i][j])
                    if id_figure > 16:
                        self.canvas.coords(id_figure, coords[1], coords[0])
                
    def get_id(self, figure):
        return self.pieces_canvas["%s%s" % (
            figure.piece, figure.color)]

    def click(self, event):
        curr_coords = self.getBoardCoords(event.x, event.y)
        self.id_target = self.canvas.find_closest(event.x, event.y)
        self.target_location = self.canvas.coords(self.id_target)
        self.clicked_item = self.board.field[curr_coords[0]][curr_coords[1]]

    def move(self, event):
        if self.id_target[0] > 16:
            self.canvas.coords(self.id_target[0],
                event.x - self.square_size / 2,
                    event.y - self.square_size / 2)
 
    def release(self, event):
        if self.id_target[0] > 16:
            self.curr_coords = self.getBoardCoords(event.x, event.y)
            self.prev_coords = self.getBoardCoords(self.target_location[0],
                            self.target_location[1])

            curr_coords = self.getBoardCoords(event.x, event.y)
            prev_coords = self.getBoardCoords(self.target_location[0],
                            self.target_location[1])

            if self.board.field[
                prev_coords[0]][prev_coords[1]].check_move_possible(
                    prev_coords, curr_coords, self.board):

                self.board_abbriviations = self.board.get_board_abbriviations()
                self.movePiece(prev_coords, curr_coords)
                self.player1Turn = not self.player1Turn

            self.board.print_board()
            print('\n')
            self.board.winner()
            bot_move = self.max_alpha_beta(-99999999, 99999999, 5)
            print(bot_move)

            #self.movePiece (bot_move[3], (bot_move[1], bot_move[2]))
            self.movePiece(self.best_move[0], self.best_move[1])
            self.refresh()

    def movePiece(self, prev_coords, curr_coords):
        # Moving item in board.field, setting previous position to 0
        if self.board.field[curr_coords[0]][curr_coords[1]] == 0:
            self.board.field[curr_coords[0]][curr_coords[1]] = self.board.field[prev_coords[0]][prev_coords[1]]
            self.board.field[prev_coords[0]][prev_coords[1]] = 0

        else:
            # Return item to default position
            pos = self.board.field[
                    curr_coords[0]][curr_coords[1]].abbriviation
            default_coords = self.board.get_default_coords(pos)

            self.board.field[
                curr_coords[0]][curr_coords[1]].in_board = False

            a = default_coords[0]
            b = default_coords[1]
            c = curr_coords[0]
            d = curr_coords[1]
            self.board.field[a][b] = self.board.field[c][d]

            self.board.field[curr_coords[0]][curr_coords[1]] = self.board.field[prev_coords[0]][prev_coords[1]]
            self.board.field[prev_coords[0]][prev_coords[1]] = 0

        if not self.board.field[curr_coords[0]][curr_coords[1]].in_board:
            self.board.field[curr_coords[0]][curr_coords[1]].in_board = True

    def undoMove(self, prev_coords, curr_coords, prev_board):
        if prev_board[curr_coords[0]][curr_coords[1]] == '0':
            self.board.field[prev_coords[0]][prev_coords[1]] = self.board.field[curr_coords[0]][curr_coords[1]]
            self.board.field[curr_coords[0]][curr_coords[1]] = 0

            if prev_coords[0] == 0 or prev_coords[0] == 5:
                self.board.field[prev_coords[0]][prev_coords[1]].in_board = False
        else:
            pos = prev_board[
                    curr_coords[0]][curr_coords[1]]
            default_coords = self.board.get_default_coords(pos)

            a = default_coords[0]
            b = default_coords[1]
            c = curr_coords[0]
            d = curr_coords[1]

            self.board.field[prev_coords[0]][prev_coords[1]] = self.board.field[curr_coords[0]][curr_coords[1]]
            self.board.field[c][d] = self.board.field[a][b]
            self.board.field[a][b] = 0

            self.board.field[curr_coords[0]][curr_coords[1]].in_board = True

    def getCoords(self, x, y):
        return(self.square_size * x + 2, self.square_size * y + 2)

    def getBoardCoords(self, x, y):
        return(int(y // self.square_size), int(x // self.square_size))

    def drawBoard(self):
        color = self.color1
        for i in range(1, self.rows + 1):
            color = self.color2 if color == self.color1 else self.color1
            for j in range(1, self.columns + 1):
                color = self.color2 if color == self.color1 else self.color1
                x1 = j * self.square_size - self.square_size
                # (self.square_size * (j - 1))

                y1 = i * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", fill=color)

    def addpiece(self, figure, x, y):
        imageName = "%s%s" % (figure.piece, figure.color)
        image = Image.open(self.imageHelper.getImageData(imageName))
        resize_image = image.resize(
            (self.square_size - 4, self.square_size - 4))
        self.icons[imageName] = ImageTk.PhotoImage(resize_image)
        self.pieces_canvas[imageName] = self.canvas.create_image(
            x, y, image=self.icons[imageName], 
            tags=figure.abbriviation, anchor="nw")

    def draw_pieces(self):
        x = 2
        y = 2 

        half = len(self.figures) // 2
        for i in range(0, half):
            self.addpiece(self.figures[i], x, y)
            self.addpiece(self.figures[i + half], x, y + self.square_size * 5)
            x += self.square_size


    def max_alpha_beta(self, alpha, beta, depth):
        result = self.board.winner()
        if result == 'Player 1 wins':
            return -10000
        elif result == 'Bot wins':
            return 10000
        elif depth ==  0:
            return self.board.compute_rating(True)

        possible_moves = self.board.get_possible_moves(True)

        for move in possible_moves:
            for location_to in move[1]:
                board_abbriviations_temp = self.board.get_board_abbriviations()
                self.movePiece(move[0], location_to)

                rating = self.min_alpha_beta(alpha, beta, depth-1)

                self.undoMove(move[0], location_to, board_abbriviations_temp)

                if rating > alpha:
                    alpha = rating

                    if depth == 5:
                        self.best_move = (move[0], location_to)

                if alpha >= beta:
                    return alpha

        return alpha

    def min_alpha_beta(self, alpha, beta, depth):
        result = self.board.winner()
        if result == 'Player 1 wins':
            return -10000
        elif result == 'Bot wins':
            return 10000
        elif depth ==  0:
            return self.board.compute_rating(False)

        possible_moves = self.board.get_possible_moves(False)

        for move in possible_moves:
            for location_to in move[1]:
                board_abbriviations_temp = self.board.get_board_abbriviations()
                self.movePiece(move[0], location_to)

                rating = self.max_alpha_beta(alpha, beta, depth-1)

                self.undoMove(move[0], location_to, board_abbriviations_temp)

                if rating <= beta:
                    beta = rating

                if alpha >= beta:
                    return beta

        return beta