import Board as Board
import tkinter as tk
import figures.Figure as Figure


from PIL import Image, ImageTk

class BoardGuiTk(tk.Tk):
    rows = 4
    columns = 4

    color1 = "white"
    color2 = "gray"

    icons = {}

    def __init__(self, square_size=64):
        super().__init__()
        self.board = Board.Board()

        self.square_size = square_size
        canvas_width = self.columns * square_size
        canvas_height = (self.rows * square_size) + square_size  * 2

        # configure the root window
        self.title('EasyChess App')
        #self.geometry('600x800')

        self.canvas = tk.Canvas(self, width=canvas_width, height=canvas_height, background="gray")
        self.canvas.pack(fill="both", expand=1)
        self.fig = Figure.Bishop("white")


    def drawBoard (self):
        color = self.color1
        for i in range (1, self.rows+1):
            color = self.color2 if color == self.color1 else self.color1
            for j in range (1, self.columns+1):
                color = self.color2 if color == self.color1 else self.color1
                x1 = j * self.square_size - self.square_size ##(self.square_size * (j - 1))
                y1 = (i * self.square_size - self.square_size) + 64
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)


    def draw_pieces(self):
        filename = "images/icons/rookblue.png"

        image = Image.open(filename)
        resize_image = image.resize((60, 60))
        self.icons[filename] = ImageTk.PhotoImage(resize_image)

        self.canvas.create_image(2, 2, image=self.icons[filename], anchor="nw")

        """ filename = "images/icons/pawnblue.png"

        image = Image.open(filename)
        resize_image = image.resize((60, 60))
        self.icons[filename] = ImageTk.PhotoImage(resize_image)

        self.canvas.create_image(66, 2, image=self.icons[filename], anchor="nw") """

        ##TODO Make the full drawing of the pieces in one call
        ##for i in range (8):




                
