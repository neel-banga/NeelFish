import board_moves
import pprint
import copy
import random
import time


DEPTH = 2

def log(arg):
    pprint.pprint(arg)


def chessb(board):
    print('\n')
    print('\n')

    chess_pieces = {
        0: ".",
        -1: "♟️",
        -3: "♞",
        -3.5: "♝",
        -9: "♛",
        -5: "♜",
        float('-inf'): "♚",
        1: "♙",
        3: "♘",
        3.5: "♗",
        9: "♕",
        5: "♖",
        float('inf'): "♔",
    }

    print("  a b c d e f g h")
    for i in range(8):
        print(8 - i, end=" ")
        for j in range(8):
            piece = chess_pieces.get(board[i][j], " ")
            print(piece, end=" ")
        print()
    
    print('\n')
    print('\n')

'''def evaluate_board(board, turn):
    our_pieces = 0
    their_pieces = 0
    score = 0
    opp_king_dead = True
    king_dead = True

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
        return float('-inf')

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

    return score'''

def evaluate_board(board, _): # you can remove this ot var
    score = 0
    for row in board:
        for piece in row:
            score += piece

    return score



def select_best_move(board, turn):
    moves = board_moves.generate_all_moves(board, turn)

    random.shuffle(moves)

    if not moves:
        return False
    
    highest_score = float('-inf')
    highest_board = None  # Initialize with None
    for move in moves:
        new_board = copy.deepcopy(board)
        start_pos, end_pos = move

        # Perform the move on the new board
        new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
        new_board[start_pos[0]][start_pos[1]] = 0

        alpha = float('-inf')
        beta = float('inf')
        
        current_score = minimax(new_board, DEPTH, turn, alpha, beta)

        if current_score > highest_score:
            highest_board = copy.deepcopy(new_board)  # Make a copy of new_board
            highest_score = current_score

    return highest_board

def select_best_move_time_limit(board, turn, duration):
    start_time = time.time()
    moves = board_moves.generate_all_moves(board, turn)

    random.shuffle(moves)

    if not moves:
        return False
    
    highest_score = float('-inf')
    highest_board = None

    for move in moves:
        if time.time() - start_time >= duration:
            break

        new_board = copy.deepcopy(board)
        start_pos, end_pos = move

        # Perform the move on the new board
        new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
        new_board[start_pos[0]][start_pos[1]] = 0

        alpha = float('-inf')
        beta = float('inf')
        
        current_score = minimax_time_limit(new_board, DEPTH, turn, alpha, beta, start_time, duration)

        if current_score > highest_score:
            highest_board = copy.deepcopy(new_board)
            highest_score = current_score

    return highest_board

def minimax(board, depth, turn, alpha, beta):

    if depth == 0 or board_moves.is_checkmate(board, turn*-1) or board_moves.is_checkmate(board, turn) or board_moves.is_draw(board):
        return evaluate_board(board, turn)
    
    moves = board_moves.generate_all_moves(board, turn)

    if turn == 1:
        max_eval = float('-inf')
        max_eval = float('inf')

        for move in moves:
            new_board = copy.deepcopy(board)
            start_pos, end_pos = move
            new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
            new_board[start_pos[0]][start_pos[1]] = 0
            eval = minimax(new_board, depth-1, turn*-1, alpha, beta)
            max_eval = max(max_eval, eval) # Highest EVAL
            #max_eval = eval # END EVAL 

            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        
        return max_eval

    else:
        max_eval = float('inf')

        for move in moves:
            new_board = copy.deepcopy(board)
            start_pos, end_pos = move
            new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
            new_board[start_pos[0]][start_pos[1]] = 0
            eval = minimax(new_board, depth-1, turn*-1, alpha, beta)
            min_eval = min(max_eval, eval) # Highest EVAL
            #max_eval = eval # END EVAL  
            beta = min(beta, eval)
            if beta <= alpha:
                break       

        return min_eval
    
def minimax_time_limit(board, depth, turn, alpha, beta, start_time, duration):
    try:
        if time.time() - start_time >= duration:
            return evaluate_board(board, turn)

        if depth == 0 or board_moves.is_checkmate(board, turn*-1) or board_moves.is_checkmate(board, turn) or board_moves.is_draw(board):
            return evaluate_board(board, turn)
        
        moves = board_moves.generate_all_moves(board, turn)

        if turn == 1:
            max_eval = float('-inf')

            for move in moves:
                new_board = copy.deepcopy(board)
                start_pos, end_pos = move
                new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
                new_board[start_pos[0]][start_pos[1]] = 0
                eval = minimax_time_limit(new_board, depth-1, turn*-1, alpha, beta, start_time, duration)
                max_eval = max(max_eval, eval)

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval

        else:
            min_eval = float('inf')

            for move in moves:
                new_board = copy.deepcopy(board)
                start_pos, end_pos = move
                new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
                new_board[start_pos[0]][start_pos[1]] = 0
                eval = minimax_time_limit(new_board, depth-1, turn*-1, alpha, beta, start_time, duration)
                min_eval = min(min_eval, eval)

                beta = min(beta, eval)
                if beta <= alpha:
                    break       

            return min_eval
    except:
        return evaluate_board(board, turn)