import board_moves
import pprint

def evaluate_board(board, turn):
    our_pieces = 0
    their_pieces = 0
    score = 0

    for row in range(8):
        for col in range(8):
            piece = board[row][col]

            if piece == float('inf'):
                king_dead = False
            if piece == float('-inf'):
                opp_king_dead = False

    if king_dead:
        return float('inf')
    if opp_king_dead:
        return -float('inf')

    if board_moves.is_checkmate(board, turn):
        return -float('inf')
    if board_moves.is_checkmate(board, -1 * turn):
        return float('inf')

    if board_moves.is_draw(board):
        return 0

    for row in board:
        for piece in row:
            if piece < 0 and piece != float('-inf'):
                our_pieces += piece
            
            if piece > 0 and piece != float('inf'):
                their_pieces += piece

    score += 10 if board_moves.is_king_in_check(board, -1 * turn) else 0
    score -= 10 if board_moves.is_king_in_check(board, turn) else 0

    score += (our_pieces * 100)
    score -= (their_pieces * 100)

    return score

board = [[0, 0, -1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, float('inf'), 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [float('-inf'), 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]

board = board_moves.pawn_promotion(board)
print(evaluate_board(board, -1))