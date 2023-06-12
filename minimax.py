import board_moves
from board_moves import chessb
import pprint


MINIMAX_DEPTH = 5

# lets start with a very basic eval board function - just get whites pieces subtracted by blacks pieces so player 1 pieces - player 2 pieces 
# but this is a trick since the peices are negative we actually add them

def eval_board(board):
    score = 0

    for i in board:
        for x in i:
            if x != float('inf') and x != float('-inf'):
                score += x

    return score

# WE DONT CARE ABOUT THE BEST BOARD WE ARE EVALUATING POSITIONS, MINIMAX SIMPLY EVALUATIES POSITIONS AND THEN WE CREATE ANOTHER FUNCTION THAT COMPARES EVALUTIOATNS AND FINDS THE BEST BOARD OMG

def minimax(board, depth, player):

    score = 0

    if depth == 0 or board_moves.is_checkmate(board, player) or board_moves.is_checkmate(board, player*-1) or board_moves.is_draw(board):
        return eval_board(board)

    moves = board_moves.generate_all_moves(board, player)

    if player == 1: # then we are maximizing 
        score = float('-inf')
        for i in moves:
            
            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])

            white_value = minimax(child, depth-1, player*-1)

            if white_value > score:
                score = white_value

        return score

    elif player == -1: # then we are minimizing
        score = float('inf')
        for i in moves:

            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
            black_value = minimax(child, depth-1, player*-1)
            

            if black_value < score:
                score = black_value

            return score

def select_best_child(board, player):

    big_value = float('inf')*player*-1
    big_board = []

    moves = board_moves.generate_all_moves(board, player)
    
    for i in moves:
        child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
        value = minimax(child, MINIMAX_DEPTH, player)

        if value > big_value and player == 1:
            big_value = value
            big_board = child

        if value < big_value and player == -1:
            big_value = value
            big_board = child


    return big_board


turn = 1
board = board_moves.create_board()

chessb(board)
while True:
    board = select_best_child(board, turn)
    chessb(board)
    turn *= -1

#print(minimax(board, 100, 1)) # it gives us accurate stuff seeing like 3-5 moves in the future at 9 its getting buggy unsure whether this is incorrect minimax or?


# issues:
'''
-bishops jumpin over peices
- your not checking for pawn promotion or checkmate
- checkmate isn't a heuristic for the EVAL board function
'''