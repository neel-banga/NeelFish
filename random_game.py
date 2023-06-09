import board_moves
import random
import sys
from board_moves import chessb

board = board_moves.create_board()

TURN = 1

while True:
    chessb(board)

    moves = board_moves.generate_all_moves(board, TURN)

    rmlist = []

    for i in range(len(moves)):
        move = moves[i]
        capture = board_moves.is_captured(board, TURN, move[1][0], move[1][1])
        moves[i] = (capture,) + move

    if not moves:
        if board_moves.is_checkmate(board, TURN):
            if TURN == -1:
                print('CHECKMATE - White Wins!')
                sys.exit()
            elif TURN == 1:
                print('CHECKMATE - Black Wins!')

            chessb(board)
            break

        if board_moves.is_draw(board):
            print('DRAW')
            chessb(board)
            break       

    try: move = random.choice(moves)
    except: 
        if board_moves.is_checkmate(board, TURN):
            if TURN == -1:
                print('CHECKMATE - White Wins!')
                sys.exit()
            elif TURN == 1:
                print('CHECKMATE - Black Wins!')

            chessb(board)
            break

        if board_moves.is_draw(board):
            print('DRAW')
            chessb(board)
            break      


    board = board_moves.move_piece(board, move[1][0], move[1][1], move[2][0], move[2][1])

    TURN *= -1

    board = board_moves.pawn_promotion(board)

    if board_moves.is_checkmate(board, TURN):
        print('CHECKMATE')
        chessb(board)
        break

    if board_moves.is_draw(board):
        print('DRAW')
        chessb(board)
        break
