"""
Unit tests for the board
"""
#We add all the files in the app directory so that they can be found
from sys import path
from tkinter.constants import FALSE, TRUE



#This works for CI, comment this when running locally
from app.views.figures.Figure import Figure as Figure
from app.views.figures.Figure import Rook as Rook
from app.views.figures.Figure import Bishop as Bishop
from app.views.figures.Figure import Knight as Knight
from app.views.figures.Figure import Pawn as Pawn

from app.views.Board import Board

class TestBoard:


    """
        Every test here is based on the board.field coordinates, where we check if some initial moves are possible to be made
    """

##ROOK TESTS
    #Check horizontally from left to right
    def test_rook_left_to_right(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [1][0] = board.field [0][0]


        curr_pos = 1
        for x in [1,2,3,4]:
            for y in [1,2,3]:
                assert board.field [curr_pos][0].check_move_possible((curr_pos,0), (x, y), board) == True
            
            board.field [curr_pos][0] = 0
            curr_pos += 1
            board.field [curr_pos][0] = board.field [0][0]

    #Check horizontally from right to left
    def test_rook_right_to_left(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [1][3] = board.field [0][0]

        curr_pos = 1
        for x in [1,2,3,4]:
            for y in [0,1,2]:
                assert board.field [curr_pos][3].check_move_possible((curr_pos,3), (x, y), board) == True
            
            board.field [curr_pos][3] = 0
            curr_pos += 1
            board.field [curr_pos][3] =  board.field [0][0]

    #Check horizontally from top to bottom
    def test_rook_top_to_bottom(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [1][0] = board.field [0][0]

        curr_pos = 0
        for y in [0,1,2,3]:
            for x in [2,3,4]:
                assert board.field [1][curr_pos].check_move_possible((1,curr_pos), (x, y), board) == True
            
            if curr_pos < 3:
                board.field [1][curr_pos] = 0
                curr_pos += 1
                board.field [1][curr_pos] = board.field [0][0]

    #Check horizontally from bottom to top
    def test_rook_bottom_to_top(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [4][0] = board.field [0][0]

        curr_pos = 0
        for y in [0,1,2,3]:
            for x in [1,2,3]:
                assert board.field [4][curr_pos].check_move_possible((4,curr_pos), (x, y), board) == True
            
            if curr_pos < 3:
                board.field [4][curr_pos] = 0
                curr_pos += 1
                board.field [4][curr_pos] = board.field [0][0]


##BISHOP TESTS
    #Check diagonally
    def test_bishop_main_diagonals(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [1][0] = board.field [0][1]
        moves = ((2,1),(3,2),(4,3))


        for x,y in moves:
            assert board.field [1][0].check_move_possible((1,0), (x, y), board) == True
        

        moves = ((3,1),(2,2),(1,3))
        board.field [1][0] = 0
        board.field [4][0] = board.field [0][1]

        for x,y in moves:
            assert board.field [4][0].check_move_possible((4,0), (x, y), board) == True

##KNIGHT TESTS
    #Check some initial L moves
    def test_knight_l_moves(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                    Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [2][1] = board.field [0][2]
        moves = ((1,3),(3,3),(4,2),(4,0))


        for x,y in moves:
            assert board.field [2][1].check_move_possible((2,1), (x, y), board) == True

##PAWN TESTS
    #Check some initial L moves
    def test_pawn_moves(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                    Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        board.field [1][0] = board.field [0][3]

        assert board.field [1][0].check_move_possible((1,0), (2,0), board) == True



##COLLISION TESTS
    def test_collision_rook(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                    Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        #Adding rook to board
        board.field [1][0] = board.field [0][0]
        board.field [1][0].in_board = True

        #Adding other pieces to board and checking collision
        board.field [1][3] = board.field [0][1]
        board.field [1][2] = board.field [0][1]
        board.field [2][0] = board.field [0][1]
        board.field [4][0] = board.field [0][1]

        assert board.field [1][0].check_move_possible((1,0), (1,3), board) == False
        assert board.field [1][0].check_move_possible((1,0), (1,2), board) == False
        assert board.field [1][0].check_move_possible((1,0), (2,0), board) == False
        assert board.field [1][0].check_move_possible((1,0), (4,0), board) == False

    def test_collision_bishop(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        #Adding bishop to board
        board.field [1][0] = board.field [0][1]
        board.field [1][0].in_board = True

        #Adding other pieces to board and checking collision
        board.field [1][3] = board.field [0][3]
        assert board.field [1][0].check_move_possible((1,0), (1,3), board) == False

        board.field [2][1] = board.field [0][1]
        assert board.field [1][0].check_move_possible((1,0), (2,1), board) == False

        board.field [3][2] = board.field [0][2]
        assert board.field [1][0].check_move_possible((1,0), (3,2), board) == False

        board.field [4][3] = board.field [5][3]
        assert board.field [1][0].check_move_possible((1,0), (4,3), board) == False

    def test_collision_knight(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        #Adding knight to board
        board.field [1][0] = board.field [0][2]
        board.field [1][0].in_board = True

        #Adding other pieces to board and checking collision
        board.field [2][3] = board.field [0][3]
        assert board.field [1][0].check_move_possible((1,0), (2,3), board) == False

        board.field [3][1] = board.field [0][1]
        assert board.field [1][0].check_move_possible((1,0), (3,1), board) == False


        assert board.field [1][0].check_move_possible((1,0), (1,3), board) == False
        assert board.field [1][0].check_move_possible((1,0), (5,3), board) == False

    def test_collision_pawn(self):
        figures = [Rook("white"), Bishop("white"), Knight("white"), Pawn("white"),

                        Rook("blue"), Bishop("blue"), Knight("blue"), Pawn("blue")]

        board = Board(figures)

        #Adding pawns to board
        board.field [1][0] = board.field [0][3]
        board.field [1][0].in_board = True

        #Adding other pieces to board and checking collision
        board.field [2][0] = board.field [5][1]
        assert board.field [1][0].check_move_possible((1,0), (2,0), board) == False


        assert board.field [1][0].check_move_possible((1,0), (1,1), board) == False

        
        
        
        





    
        
        

        
