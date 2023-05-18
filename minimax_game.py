import minimax_bot
import board_moves
from minimax_bot import log

board = board_moves.create_board()

turn = 1

while True:

    if board_moves.is_checkmate(board, 1) or board_moves.is_checkmate(board, -1) or board_moves.is_draw(board):

        if board_moves.is_checkmate(board, 1):
            print('White Wins!')

        elif board_moves.is_checkmate(board, -1):
            print('Black Wins')

        else:
            print('Draw')

        log(board)

    board = board_moves.pawn_promotion(board)

    log(board)
    board = minimax_bot.select_best_move(board, turn)
    turn *= -1