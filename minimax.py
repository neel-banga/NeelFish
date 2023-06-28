import board_moves
from board_moves import chessb
import time
from tqdm import tqdm

MAX_TIME = 30
MINIMAX_DEPTH = 4

def set_max_time(x):
    global MAX_TIME
    MAX_TIME = x

def set_depth(x):
    global MINIMAX_DEPTH
    MINIMAX_DEPTH = x

def get_max_time():
    return MAX_TIME

def get_depth():
    return MINIMAX_DEPTH

# lets start with a very basic eval board function - just get whites pieces subtracted by blacks pieces so player 1 pieces - player 2 pieces 
# but this is a trick since the peices are negative we actually add them

def eval_board(board):
    score = 0

    if board_moves.is_checkmate(board, 1):
        return float('inf')
    if board_moves.is_checkmate(board, -1):
        return float('-inf')
    if board_moves.is_draw(board):
        return 0

    for i in board:
        for x in i:
            if x != float('inf') and x != float('-inf') and x != 0:
                score += x

    return score

def reorder_moves(board, moves):

    # The reason I go from 0 to 9 is because it's most likely most moves will be no captures and pawn captures
    # This will make the program faster as the rest of the statements are elif statements

    nine_list = []
    five_list = []
    three_list = []
    one_list = []
    zero_list = []

    for move in moves:
        if board[move[1][0]][move[1][1]] == 0:
            zero_list.append(move)
        elif board[move[1][0]][move[1][1]] == 1:
            one_list.append(move)
        elif board[move[1][0]][move[1][1]] == 3:
            three_list.append(move)
        elif board[move[1][0]][move[1][1]] == 5:
            five_list.append(move)
        elif board[move[1][0]][move[1][1]] == 9:
            nine_list.append(move)

    new_moves = nine_list + five_list + three_list + one_list + zero_list
    return new_moves

def iterative_deepening(board, player, TIME_LIMIT):
    best_move = None
    start_time = time.time()

    for depth in range(1, MINIMAX_DEPTH + 1):
        score = minimax(board, depth, player, float('-inf'), float('inf'))

        best_move = score

        # Check if the elapsed time exceeds the maximum time limit
        elapsed_time = time.time() - start_time
        if elapsed_time >= TIME_LIMIT:
            break

    return best_move


# WE DONT CARE ABOUT THE BEST BOARD WE ARE EVALUATING POSITIONS, MINIMAX SIMPLY EVALUATIES POSITIONS AND THEN WE CREATE ANOTHER FUNCTION THAT COMPARES EVALUTIOATNS AND FINDS THE BEST BOARD OMG

def minimax(board, depth, player, alpha, beta):

    score = 0

    if depth == 0 or board_moves.is_checkmate(board, player) or board_moves.is_checkmate(board, player*-1) or board_moves.is_draw(board):
        return eval_board(board)
    
    moves = board_moves.generate_all_moves(board, player)
    reorder_moves(board, moves)

    if player == 1: # then we are maximizing 
        score = float('-inf')
        for i in moves:
            
            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
            child = board_moves.pawn_promotion(child)

            white_value = minimax(child, depth-1, player*-1, alpha, beta)

            score = max(white_value, score)              
            alpha = max(alpha, score)

            if beta <= alpha:
                break

        return score

    elif player == -1: # then we are minimizing
        score = float('inf')
        for i in moves:

            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
            child = board_moves.pawn_promotion(child)

            black_value = minimax(child, depth-1, player*-1, alpha, beta)

            score = min(black_value, score)
            beta = min(score, beta)

            if beta <= alpha:
                break

        return score
    

def minimax_pre_pruning(board, depth, player):

    score = 0

    if depth == 0 or board_moves.is_checkmate(board, player) or board_moves.is_checkmate(board, player*-1) or board_moves.is_draw(board):
        return eval_board(board)
    
    moves = board_moves.generate_all_moves(board, player)
    reorder_moves(board, moves)

    if player == 1: # then we are maximizing 
        score = float('-inf')
        for i in moves:
            
            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
            child = board_moves.pawn_promotion(child)

            white_value = minimax_pre_pruning(child, depth-1, player*-1)

            score = max(white_value, score)

        return score

    elif player == -1: # then we are minimizing
        score = float('inf')
        for i in moves:

            child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
            child = board_moves.pawn_promotion(child)

            black_value = minimax_pre_pruning(child, depth-1, player*-1)

            score = min(black_value, score)

        return score

def select_best_child(board, player):

    big_value = float('inf')*player*-1
    big_board = []

    moves = board_moves.generate_all_moves(board, player)
    reorder_moves(board, moves) # Instead of just shuffling moves lets check if they contain captures and then re-order moves
    
    for i in tqdm(moves):
        child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
        child = board_moves.pawn_promotion(child)
        value = minimax_pre_pruning(child, MINIMAX_DEPTH, player)#, float('-inf'), float('inf'))

        if value > big_value and player == 1:
            big_value = value
            big_board = child

        if value < big_value and player == -1:
            big_value = value
            big_board = child

    return big_board

def select_best_child_time_limit(board, player, time):

    big_value = float('inf')*player*-1
    big_board = []

    moves = board_moves.generate_all_moves(board, player)
    reorder_moves(board, moves) # Instead of just shuffling moves lets check if they contain captures and then re-order moves
    
    for i in tqdm(moves):
        child = board_moves.move_piece(board, i[0][0], i[0][1], i[1][0], i[1][1])
        child = board_moves.pawn_promotion(child)
        value = iterative_deepening(child, player, time)

        if value > big_value and player == 1:
            big_value = value
            big_board = child

        if value < big_value and player == -1:
            big_value = value
            big_board = child

    return big_board

def play_against_user():

    turn = -1  # I have swapped the white and black
    board = board_moves.create_board()
    chessb(board)
    print('Enter your moves in coordinate format (previous move), (next move) ')
    print('For example, a6,a7')

    values = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    while True:

        if board_moves.is_checkmate(board, turn):
            if turn == -1:
                print('CHECKMATE - White Wins!')
            elif turn == 1:
                print('CHECKMATE - Black Wins!')

            chessb(board)
            break

        if board_moves.is_draw(board):
            print('DRAW')
            chessb(board)
            break

        while True:
            move = input('Your Move: ').replace(' ', '')
            move1, move2 = move.split(',')

            prev0, prev1 = abs(7-(int(move1[1])-1)), values[move1[0]],
            next0, next1 = abs(7-(int(move2[1])-1)), values[move2[0]]

            print((prev0, prev1), (next0, next1))

            moves = board_moves.generate_all_moves(board, turn)
            
            if ((prev0, prev1), (next0, next1)) in moves:break
            else: print('That move is not valid!')

        board = board_moves.move_piece(board, prev0, prev1, next0, next1)

        print('-- Your Move --')

        chessb(board)

        turn *= -1

        board = select_best_child(board, turn)
        print('-- The Computer Has Played --')
        chessb(board)

        turn *= -1

def play_against_itself():
    turn = -1
    board = board_moves.create_board()

    chessb(board)
    while True:
        board = select_best_child(board, turn)
        chessb(board)
        turn *= -1


def play_against_user_time_limit():

    turn = -1  # I have swapped the white and black
    board = board_moves.create_board()
    chessb(board)
    print('Enter your moves in coordinate format (previous move), (next move) ')
    print('For example, a6,a7')

    values = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

    while True:

        if board_moves.is_checkmate(board, turn):
            if turn == -1:
                print('CHECKMATE - White Wins!')
            elif turn == 1:
                print('CHECKMATE - Black Wins!')

            chessb(board)
            break

        if board_moves.is_draw(board):
            print('DRAW')
            chessb(board)
            break


        while True:
            move = input('Your Move: ').replace(' ', '')
            move1, move2 = move.split(',')

            prev0, prev1 = abs(7-(int(move1[1])-1)), values[move1[0]],
            next0, next1 = abs(7-(int(move2[1])-1)), values[move2[0]]

            print((prev0, prev1), (next0, next1))

            moves = board_moves.generate_all_moves(board, turn)
            
            if ((prev0, prev1), (next0, next1)) in moves:break
            else: print('That move is not valid!')

        board = board_moves.move_piece(board, prev0, prev1, next0, next1)

        print('-- Your Move --')

        chessb(board)

        turn *= -1

        board = select_best_child_time_limit(board, turn, MAX_TIME)
        print('-- The Computer Has Played --')
        chessb(board)

        turn *= -1

def play_against_itself_time_limit():
    turn = -1
    board = board_moves.create_board()

    chessb(board)
    while True:
        board = select_best_child_time_limit(board, turn)
        chessb(board)
        turn *= -1