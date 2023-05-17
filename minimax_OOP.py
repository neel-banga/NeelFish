import board_moves
import pprint
import copy

class ChessTree:
    def __init__(self, board, turn) -> None:
        self.board = board
        self.turn = turn

    def evaluate_board(self):
        our_pieces = 0
        their_pieces = 0
        score = 0

        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]

                if piece == float('inf'):
                    king_dead = False
                if piece == float('-inf'):
                    opp_king_dead = False

        if king_dead:
            return float('inf')
        if opp_king_dead:
            return float('-inf')

        if board_moves.is_checkmate(self.board, self.turn):
            return -float('inf')
        if board_moves.is_checkmate(self.board, -1 * self.turn):
            return float('inf')

        if board_moves.is_draw(self.board):
            return 0

        for row in self.board:
            for piece in row:
                if piece < 0 and piece != float('-inf'):
                    our_pieces += piece
                
                if piece > 0 and piece != float('inf'):
                    their_pieces += piece

        score += 10 if board_moves.is_king_in_check(self.board, -1 * self.turn) else 0
        score -= 10 if board_moves.is_king_in_check(self.board, self.turn) else 0

        score += (our_pieces * 100)
        score -= (their_pieces * 100)

        return score
    
    def select_best_move(self):
        moves = board_moves.generate_all_moves(board)

        if not moves:
            return False # If False we break and check for mate - we should probably do that before
        

        boards = []
        for move in moves:
            new_board = copy.deepcopy(board)
            start_pos, end_pos = move

            # Perform the move on the new board
            new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
            new_board[start_pos[0]][start_pos[1]] = 0
            
            boards.append(self.evaluate_board(new_board), new_board)

        boards.sort()

        # If max player take 0th elem if not min take -1 elem


board = [[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, -1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, float('inf'), 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 5, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, float('-inf'), 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]

board = board_moves.pawn_promotion(board)

def minimax(board, depth, max_player):
    if depth == 0 or board_moves.is_checkmate == True or board_moves.is_draw == True:
        return

# does it really make sense to use OOP 
# IMO Not really