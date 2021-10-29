import tkinter
class Board():
    def __init__(self, figures):
        self.STARTING = "rbkp-RBKP"
        self.field = []
        self.reset (figures)
        self.player1 = set(['R','B','K','P'])
        self.player2 = set(['r','b','k','p'])

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
        self.player1 = self.field[0]
        self.player2 = self.field[len(self.field)-1]

    def get_default_coords (self, letter):
        if str.islower(letter):
            return 0, self.STARTING.index(letter)
        
        return 5, self.STARTING.index(letter) - 5

    #helper function to decide whether who won
    def check_winner(self,array):
        if(all(array)):
            if set(array)==set(self.player1):
                return "Player 1 wins"
            if set(array)==set(self.player2):
                return "Player 2 wins"

    def winner(self):
        print("WORKING")
        #checking the rows
        for i in range(1,len(self.field)-1):
            row=[(str(x) if x!=0 else x) for x in self.field[i]]
            #print(row)
            #print(all(row))
            if(self.check_winner(row)):
                print(self.check_winner(row))
                return(True,self.check_winner(row))
        
        #Checking the first diagonal
        diag1 = [((str(self.field[x][x-1])) if self.field[x][x-1]!=0 else 0) for x in range(1,len(self.field)-1)]
        #print(diag1)
        if(self.check_winner(diag1)):
            print(self.check_winner(diag1))
            return(True,self.check_winner(diag1))
        
        #Checking the second diagonal
        diag2 =[((str(self.field[x][len(self.field[x])-x])) if self.field[x][len(self.field[x])-x]!=0 else 0) for x in range(1,len(self.field)-1)]
        if(self.check_winner(diag2)):
            print(self.check_winner(diag2))
            return(True,self.check_winner(diag2))

        #checking the columns
        for i in range(0,len(self.field[0])):
            col=[]
            col.append(str(self.field[1][i]) if self.field[1][i]!=0 else 0 )
            col.append(str(self.field[2][i]) if self.field[2][i]!=0 else 0 )
            col.append(str(self.field[3][i]) if self.field[3][i]!=0 else 0 )
            col.append(str(self.field[4][i]) if self.field[4][i]!=0 else 0 )
            if(self.check_winner(col)):
                print(self.check_winner(col))
                return(True,self.check_winner(col))



        







            



"""
Board
R, B, K, P - for White pieces
r, b, k, p - for Black pieces

r - rook
b - bishop
k - knight
p - pawn

"""