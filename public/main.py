#We add all the files in the app directory so that they can be found

from sys import path

path.append('..\\app\\views')

from BoardGuiTk import BoardGuiTk



if __name__ == "__main__":

    boardGUI = BoardGuiTk ()

    boardGUI.drawBoard ()

    boardGUI.draw_pieces ()

    boardGUI.mainloop ()