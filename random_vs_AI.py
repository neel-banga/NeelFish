import minimax
import board_moves
from board_moves import chessb
import random
import board_moves

board = board_moves.create_board()

turn = -1

while True:

    if board_moves.is_checkmate(board, 1) or board_moves.is_checkmate(board, -1) or board_moves.is_draw(board):

        if board_moves.is_checkmate(board, 1):
            print('White Wins!')

        elif board_moves.is_checkmate(board, -1):
            print('Black Wins')

        else:
            print('Draw')

        chessb(board)

    board = board_moves.pawn_promotion(board)

    chessb(board)
    
    if turn == -1:
        board = minimax.select_best_move(board, turn)

    elif turn == 1:
        moves = board_moves.generate_all_moves(board, turn)
        move = random.choice(moves)
        print(move)
        board = board_moves.move_piece(board, move[0][0], move[0][1], move[1][0], move[1][1])

    turn *= -1