import board_moves
import random
import pprint
import time

board = board_moves.create_board()

TURN = -1

while True:
    pprint.pprint(board)

    moves = board_moves.generate_all_moves(board, TURN)

    rmlist = []

    for i in range(len(moves)):
        move = moves[i]
        capture = board_moves.is_captured(board, TURN, move[1][0], move[1][1])
        moves[i] = (capture,) + move

    if not moves:
        print("No available moves.")
        pprint.pprint(board)
        break        

    move = random.choice(moves)
    board = board_moves.move_piece(board, move[1][0], move[1][1], move[2][0], move[2][1])

    TURN *= -1

    board = board_moves.pawn_promotion(board)

    if board_moves.is_checkmate(board, TURN):
        print('CHECKMATE')
        pprint.pprint(board)
        break

    if board_moves.is_draw(board):
        print('DRAW')
        pprint.pprint(board)
        break
