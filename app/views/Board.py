
class Board():
    def __init__(self, figures):
        self.STARTING = "rbkp-RBKP"
        self.field = []
        self.reset(figures)
        self.player1 = set(['r', 'b', 'k', 'p'])
        self.player2 = set(['R', 'B', 'K', 'P'])

    def print_board(self):
        for i in range(1, len(self.field) - 1):
            print([str(self.field[i][j]) for j in range(
                len(self.field[i]))], sep=", ")

    def get_board_abbriviations(self):
        abbriviations = []
        for row_field in self.field:
            row = []
            for piece in row_field:
                row.append(str(piece))
            abbriviations.append(row)

        return abbriviations

    def get_player_pieces(self, bot_move):
        pieces = []
        for i in range(0, 6):
            for j in range(0, 4):
                if self.field[i][j] != 0:
                    if(bot_move and self.field[i][j].abbriviation.isupper()) or (not bot_move and self.field[i][j].abbriviation.islower()):
                        pieces.append((i, j))

        return pieces

    def reset(self, figures):
        self.field = [[figures[0], figures[1], figures[2], figures[3]],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [figures[4], figures[5], figures[6], figures[7]]]

    def get_default_coords(self, letter):
        if str.islower(letter):
            return 0, self.STARTING.index(letter)
        
        return 5, self.STARTING.index(letter) - 5

    def compute_rating(self, bot_move):
        result = self.winner()
        if result == "Player 1 wins" and not bot_move:
            return 10000
        if result == "Bot wins" and bot_move:
            return 10000
        if result == "Player 1 wins" and bot_move:
            return -10000
        if result == "Bot wins" and not bot_move:
            return -10000
 
        player_score = 0
        bot_score = 0

        for i in range(0, 4):
            if self.field[0][i] != 0:
                player_score += 1

            if self.field[5][i] != 0:
                bot_score += 1

        if bot_move:
            return bot_score - player_score

        return player_score - bot_score

    # helper function to decide whether who won
    def check_winner(self, array):
        if(all(array)):
            if set(array) == set(self.player1):
                return "Player 1 wins"
            if set(array) == set(self.player2):
                return "Bot wins"
    
    def movePiece(self, prev_coords, curr_coords):
        # Moving item in board.field, setting previous position to 0
        if self.field[curr_coords[0]][curr_coords[1]] == 0:
            self.field[curr_coords[0]][curr_coords[1]] = self.field[prev_coords[0]][prev_coords[1]]
            self.field[prev_coords[0]][prev_coords[1]] = 0

        else:
            # Return item to default position
            pos = self.field[
                    curr_coords[0]][curr_coords[1]].abbriviation
            default_coords = self.get_default_coords(pos)

            self.field[
                curr_coords[0]][curr_coords[1]].in_board = False

            a = default_coords[0]
            b = default_coords[1]
            c = curr_coords[0]
            d = curr_coords[1]
            self.field[a][b] = self.field[c][d]

            self.field[curr_coords[0]][curr_coords[1]] = self.field[prev_coords[0]][prev_coords[1]]
            self.field[prev_coords[0]][prev_coords[1]] = 0

        if not self.field[curr_coords[0]][curr_coords[1]].in_board:
            self.field[curr_coords[0]][curr_coords[1]].in_board = True

    def undoMove(self, prev_coords, curr_coords, prev_board):
        if prev_board[curr_coords[0]][curr_coords[1]] == '0':
            self.field[prev_coords[0]][prev_coords[1]] = self.field[curr_coords[0]][curr_coords[1]]
            self.field[curr_coords[0]][curr_coords[1]] = 0

            if prev_coords[0] == 0 or prev_coords[0] == 5:
                self.field[prev_coords[0]][prev_coords[1]].in_board = False
        else:
            pos = prev_board[
                    curr_coords[0]][curr_coords[1]]
            default_coords = self.get_default_coords(pos)

            a = default_coords[0]
            b = default_coords[1]
            c = curr_coords[0]
            d = curr_coords[1]

            self.field[prev_coords[0]][prev_coords[1]] = self.field[curr_coords[0]][curr_coords[1]]
            self.field[c][d] = self.field[a][b]
            self.field[a][b] = 0

            self.field[curr_coords[0]][curr_coords[1]].in_board = True
   
    def winner(self):
        # checking the rows
        for i in range(1, len(self.field) - 1):
            row = [(str(x) if x != 0 else x) for x in self.field[i]]
            if(self.check_winner(row)):
                return self.check_winner(row)
        
        # Checking the first diagonal
        diag1 = [((str(self.field[x][x - 1])) 
                    if self.field[x][x - 1] != 0 else 0)
                        for x in range(1, len(self.field) - 1)]

        if(self.check_winner(diag1)):
            return self.check_winner(diag1)
        
        # Checking the second diagonal
        diag2 = [((str(self.field[x][len(self.field[x]) - x]))
                    if self.field[x][len(self.field[x]) - x] != 0 else 0) 
                        for x in range(1, len(self.field) - 1)]
        if(self.check_winner(diag2)):
            return self.check_winner(diag2)

        # checking the columns
        for i in range(0, len(self.field[0])):
            col = []
            col.append(str(self.field[1][i]) if self.field[1][i] != 0 else 0)
            col.append(str(self.field[2][i]) if self.field[2][i] != 0 else 0)
            col.append(str(self.field[3][i]) if self.field[3][i] != 0 else 0)
            col.append(str(self.field[4][i]) if self.field[4][i] != 0 else 0)
            if(self.check_winner(col)):
                return self.check_winner(col)

    def get_possible_moves(self, bot_move):
        pieces = self.get_player_pieces(bot_move)
        possible_moves = []
        for piece in pieces:
            moves = []
            for i in range(1, len(self.field) - 1):
                for j in range(0, 4):
                    if self.field[piece[0]][piece[1]].check_move_possible(piece, (i, j), self):
                        moves.append((i, j))

            if len(moves) != 0:
                possible_moves.append((piece, moves))
        return possible_moves


"""
Board
R, B, K, P - for White pieces
r, b, k, p - for Black pieces

r - rook
b - bishop
k - knight
p - pawn

"""
