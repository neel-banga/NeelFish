import board_moves
import random
import time
import pprint
from minimax_bot import chessb

board = board_moves.create_board()

TURN = -1

for i in range(60):

    chessb(board)
    time.sleep(1)
    
    moves = board_moves.generate_all_moves(board, TURN)

    if TURN == 1:

        for i in range(len(moves)):
            move = moves[i]
            capture = board_moves.is_captured(board, TURN, move[1][0], move[1][1])
            moves[i] = (capture,) + move

        move = moves[random.randint(0, len(moves)-1)]
        board = board_moves.move_piece(board, move[1][0], move[1][1], move[2][0], move[2][1])

    else:
        print('Here are all the possible moves: ')
        pprint.pprint(moves)
        num = int(input('Pick the number move you want to play: '))
        move = moves[num]
        print(move)
        board = board_moves.move_piece(board, move[0][0], move[0][1], move[1][0], move[1][1])

    TURN *= -1

    if board_moves.is_checkmate(board, TURN):
        if TURN == -1:
            print('YOU WIN')
        elif TURN == 1:
            print('I WIN U SUCK :)')