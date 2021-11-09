# UNCOMMENT THIS FOR LOCAL RUN
# import Board as Board
# import figures.Figure as Figure


# This works for CI, comment this when running locally
import app.views.Board as Board
import app.views.figures.Figure as Figure

import tkinter as tk
from PIL import Image, ImageTk


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

    def __init__(self, square_size=90):
        super().__init__()
        # figures instances

        self.figures = [Figure.Rook("white"), Figure.Bishop("white"),
                            Figure.Knight("white"), Figure.Pawn("white"),
                                Figure.Rook("blue"), Figure.Bishop("blue"), 
                                Figure.Knight("blue"), Figure.Pawn("blue")]

        self.board = Board.Board(self.figures)

        self.square_size = square_size
        canvas_width = self.columns * square_size
        canvas_height = (self.rows * square_size) + square_size * 2

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

    def reset(self):
        self.board.reset(self.figures)

        for figure in self.figures:
            figure.in_board = False

        self.draw_pieces()

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
        return self.pieces_canvas["images/icons/%s%s.png" % (
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
            curr_coords = self.getBoardCoords(event.x, event.y)
            prev_coords = self.getBoardCoords(self.target_location[0], 
                            self.target_location[1])

            if self.board.field[
                prev_coords[0]][prev_coords[1]].check_move_possible(
                    prev_coords, curr_coords, self.board):
                
                # Moving item in board.field, setting previous position to 0
                if self.board.field[curr_coords[0]][curr_coords[1]] == 0:
                    self.board.field[prev_coords[0]][prev_coords[1]] = 0
                    cliked = self.clicked_item
                    self.board.field[curr_coords[0]][curr_coords[1]] = cliked

                elif self.board.field[
                        prev_coords[0]][
                            prev_coords[1]].color != self.board.field[
                            curr_coords[0]][curr_coords[1]].color:

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

                    self.board.field[prev_coords[0]][prev_coords[1]] = 0
                    self.board.field[
                        curr_coords[0]][curr_coords[1]] = self.clicked_item
 
            self.board.print_board()
            print('\n')
            self.refresh()
            self.board.winner()
            
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
        filename = "images/icons/%s%s.png" % (figure.piece, figure.color)
        image = Image.open(filename)
        resize_image = image.resize(
            (self.square_size - 4, self.square_size - 4))
        self.icons[filename] = ImageTk.PhotoImage(resize_image)
        self.pieces_canvas[filename] = self.canvas.create_image(
            x, y, image=self.icons[filename], 
            tags=figure.abbriviation, anchor="nw")

    def draw_pieces(self):
        x = 2
        y = 2 

        half = len(self.figures) // 2
        for i in range(0, half):
            self.addpiece(self.figures[i], x, y)
            self.addpiece(self.figures[i + half], x, y + self.square_size * 5)
            x += self.square_size





                
