

class ChessBot:

    def __init__(self,boardGUITK):
        self.boardGUI = boardGUITK

    
    def max_alpha_beta(self, alpha, beta, depth):
        result = self.boardGUI.board.winner()
        if result == 'Player 1 wins':
            return -10000
        elif result == 'Bot wins':
            return 10000
        elif depth == 0:
            return self.boardGUI.board.compute_rating(True)

        possible_moves = self.boardGUI.board.get_possible_moves(True)

        for move in possible_moves:
            for location_to in move[1]:
                board_abbriviations_temp = self.boardGUI.board.get_board_abbriviations()
                self.boardGUI.board.movePiece(move[0], location_to)

                rating = self.min_alpha_beta(alpha, beta, depth - 1)

                self.boardGUI.board.undoMove(move[0], location_to, board_abbriviations_temp)

                if rating > alpha:
                    alpha = rating

                    if depth == 5:
                        self.boardGUI.best_move = (move[0], location_to)

                if alpha >= beta:
                    return alpha

        return alpha

    def min_alpha_beta(self, alpha, beta, depth):
        result = self.boardGUI.board.winner()
        if result == 'Player 1 wins':
            return -10000
        elif result == 'Bot wins':
            return 10000
        elif depth == 0:
            return self.boardGUI.board.compute_rating(False)

        possible_moves = self.boardGUI.board.get_possible_moves(False)

        for move in possible_moves:
            for location_to in move[1]:
                board_abbriviations_temp = self.boardGUI.board.get_board_abbriviations()
                self.boardGUI.board.movePiece(move[0], location_to)

                rating = self.max_alpha_beta(alpha, beta, depth - 1)

                self.boardGUI.board.undoMove(move[0], location_to, board_abbriviations_temp)

                if rating <= beta:
                    beta = rating

                if alpha >= beta:
                    return beta

        return beta

    def move_bot(self):
        self.max_alpha_beta(-99999999, 99999999, 5)
        self.boardGUI.board.movePiece(self.boardGUI.best_move[0], self.boardGUI.best_move[1])
        self.boardGUI.refresh()