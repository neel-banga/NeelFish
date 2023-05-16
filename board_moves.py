import copy
import sys

def create_board():

    # First, let's assign values to each piece and have those values be the pointer to the piece

    '''

    Pawn: 1 point
    Knight: 3 points
    Bishop: 3.5 points
    Rook: 5 points
    Queen: 9 points 
    King: Infinity

    '''

    # Because of the 0.5, instead of having to deal with decimal values, let's multiply all our values *2
    # This is NOT a step that is needed but simply makes our board look cleaner & allows it to remain an integer list

    '''

    Pawn: 2 point
    Knight: 6 points
    Bishop: 7 points
    Rook: 10 points
    Queen: 18 points 
    King: Infinity

    '''

    # Basic chess board layout
    '''

    board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    
    '''

    # Board with *2 layout

    board = [
    [-10, -6, -7, -18, float('-inf'), -7, -6, -10],
    [-2, -2, -2, -2, -2, -2, -2, -2],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 2, 2, 2, 2, 2, 2, 2, 2],
    [ 10, 6, 7, 18, float('inf'), 7, 6, 10]
    ]

    # Board with regular layout

    board = [
    [5, 3, 3.5, 9, float('inf'), 3.5, 3, 5],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-5, -3, -3.5, -9, float('-inf'), -3.5, -3, -5]
    ]


    # Notice we put the black pecies on the bottom and the white peices on the top, we differ them by a use of a negative sign
    # Black peices are negative while white ones are positive

    return board

def check_user_move(board, piece, old_y, old_x, y, x):


    def spot_taken():
        # Let's make sure there isn't a piece of the same color where said piece wants to move
        if piece > 0:
            if board[y][x] > 0:
                return False
            else:
                if board[y][x] < 0:
                    return False

        return True

    # Create all combos with old board and then check it in terms of new board

    def check_pawn():

        if spot_taken() == False:
            return False

        #  First let's check if it's moving left or right
        if (old_x + 1 == x and old_y == y) or (old_x - 1 == x and old_y == y):
            return True
        
        # Now let's check if it's moving up or down
        if (old_y + 1 == y and old_x == x) or (old_y - 1 == y and old_x == x):
            return True
        
        # Now let's check for takin a piece 
        if (old_x + 1 == x and old_y + 1 == y) or (old_x - 1 == x and old_y + 1 == y):
            # let's make sure a peice of the opposite color is on that position
            if board[y][x]:
                if piece > 0:
                    if board[y][x] < 0:
                        return True
                else:
                    if board[y][x] > 0:
                        return True
        
        return False

    def check_knight():
        
        if spot_taken() == False:
            return False
                
        # Check if the knight is moving 1 right/left and 2 up/down
        if (old_x - 1 == x or old_x + 1 == x) and (old_y + 2 == y or old_y - 2 == y):
            return True
        
        # Check if the knight is moving 2 right/left and 1 up/down
        if (old_x - 2 == x or old_x + 2 == x) and (old_y + 1 == y or old_y - 1 == y):
            return True
        
        return False

    def check_bishop():

        if spot_taken() == False:
            return False
        
        movement = True

        for i in range(1, 8):

            if piece > 0:
                if board[i][i] > 0:
                    movement = False

            else:
                if board[i][i] < 0:
                    movement = False

        for i in range(1, 8):

            if (old_x + i == x and old_y + i == y) and movement == True:
                return True
            
        return False

    def check_rook():

        if spot_taken() == False:
            return False

        for i in range(0, 7):

            # Make sure that rooks can't jump over pawns
            
            # For left / right

            x_movement = True
            y_movement = True

            if piece > 0:
                if board[old_y][i] > 0:
                    x_movement = False

            else:
                if board[old_y][i] < 0:
                    x_movement = False
            

            # For up / down

            if piece > 0:
                if board[i][old_x] > 0:
                    y_movement = False

            else:
                if board[i][old_x] < 0:
                    y_movement = False                

            if old_x + i == x and old_y == y and x_movement == True:
                return True

            if old_x == x and old_y + i == y and y_movement == True:
                return True
            
        return False

    def check_queen():

        if check_bishop == True:
            return True
        
        if check_rook == True:
            return True
        
        return False

    def check_king():

        if spot_taken() == False:
            return False

        # We can simply copy some of the conditionals of our pawn method
        #  First let's check if it's moving left or right
        if (old_x + 1 == x and old_y == y) or (old_x - 1 == x and old_y == y):
            return True
        
        # Now let's check if it's moving up or down
        if (old_y + 1 == y and old_x == x) or (old_y - 1 == y and old_x == x):
            return True
        
        # Now let's check for diagonal movement
        if (old_x + 1 == x and old_y + 1 == y) or (old_x - 1 == x and old_y + 1 == y):
            return True
    
    if x > 7 and x < 0:
        return False

    if board[old_y][old_x] != piece:
        return False

    if piece == 1: # pawn
        if check_pawn() == False:
            return False

    elif piece == 3: # knight
        if check_knight() == False:
            return False

    elif piece == 3.5: # bishop
        if check_bishop() == False:
            return False
    
    elif piece == 5: # rook
        if check_rook() == False:
            return False

    elif piece == 9: # queen
        if check_queen() == False:
            return False

    else:
        if check_king() == False:
            return False
    
    return True

# Now that our piece movement works, let's check if a piece of the other color is captured
# We want to not only return true BUT we want to return what that piece was & in turn it's point value

def is_captured(piece, y, x): # Taking in new positions
    if piece > 0:
        if board[y][x] < 0:
            return board[y][x]
        else:
            if board[y][x] < 0:

                # Here we're simply converting from neg. to pos. 
                # This is due to the fact that we use neg. and pos. to distiguish the color of pieices
                # But we only care about the point value now, so we want to return the POSITIVE point value

                return board[y][x]*-1 
            
    return False

def generate_pawn_moves(board, turn):
    moves = []
    
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 1 and turn == 1:  # white pawn
                # check if pawn can move one or two squares forward
                if row == 1:
                    if board[row+1][col] == 0 and board[row+2][col] == 0:
                        moves.append(((row, col), (row+2, col)))
                if row < 7 and board[row+1][col] == 0:
                    moves.append(((row, col), (row+1, col)))
                # check if pawn can capture an opponent's piece diagonally
                if row < 7 and col < 7 and board[row+1][col+1] < 0: # In the future we can do <= and the opposite for the other side
                    moves.append(((row, col), (row+1, col+1)))
                if row < 7 and col > 0 and board[row+1][col-1] < 0:
                    moves.append(((row, col), (row+1, col-1)))
                    
            elif piece == -1 and turn == -1:  # black pawn
                # check if pawn can move one or two squares forward
                if row == 6:
                    if board[row-1][col] == 0 and board[row-2][col] == 0:
                        moves.append(((row, col), (row-2, col)))
                if row > 0 and board[row-1][col] == 0:
                    moves.append(((row, col), (row-1, col)))
                # check if pawn can capture an opponent's piece diagonally
                if row > 0 and col < 7 and board[row-1][col+1] > 0:
                    moves.append(((row, col), (row-1, col+1)))
                if row > 0 and col > 0 and board[row-1][col-1] > 0:
                    moves.append(((row, col), (row-1, col-1)))
                    
    return moves

def generate_knight_moves(board, turn):
    moves = []

    def gen_moves(row, col, board):
        # Check all possible L-shaped moves
        for i, j in [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1), 
                    (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]:

            # Only consider moves that are within the bounds of the board
            if i >= 0 and i < 8 and j >= 0 and j < 8:
                if board[i][j] == 0 or board[i][j] * turn < 0:
                    moves.append(((row, col), (i, j)))

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1:
                if piece == 3: # then it's a knight
                    gen_moves(row, col, board)
            elif turn == -1:
                if piece == -3:
                    gen_moves(row, col, board)

    return moves

def generate_bishop_moves(board, turn):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1:
                if piece == 3.5:
                    t1 = True
                    t2 = True
                    t3 = True
                    t4 = True
                    for i in range(1, 8):
                        if row+i <= 7 and col+i <= 7:
                            if board[row + i][col + i] == 0 and t1:
                                moves.append(((row, col), (row + i, col + i)))
                            elif board[row + i][col + i] * turn < 0:
                                moves.append(((row, col), (row + i, col + i)))
                                t1 = False
                            else:
                                t1 = False
                        if row+i <= 7 and col-i >= 0:
                            if board[row + i][col - i] == 0 and t2:
                                moves.append(((row, col), (row + i, col - i)))
                            elif board[row + i][col - i] * turn < 0:
                                moves.append(((row, col), (row + i, col - i)))
                                t2 = False
                            else:
                                t2 = False
                        if row-i >= 0 and col+i <= 7:
                            if board[row - i][col + i] == 0 and t3:
                                moves.append(((row, col), (row - i, col + i)))
                            elif board[row - i][col + i] * turn < 0:
                                moves.append(((row, col), (row - i, col + i)))
                                t3 = False
                            else:
                                t3 = False
                        if row-i >= 0 and col-i >= 0:
                            if board[row - i][col - i] == 0 and t4:
                                moves.append(((row, col), (row - i, col - i)))
                            elif board[row - i][col - i] * turn < 0:
                                moves.append(((row, col), (row - i, col - i)))
                                t4 = False
                            else:
                                t4 = False
            elif turn == -1:
                if piece == -3.5:
                    t1 = True
                    t2 = True
                    t3 = True
                    t4 = True
                    for i in range(1, 8):
                        if row+i <= 7 and col+i <= 7:
                            if board[row + i][col + i] == 0 and t1:
                                moves.append(((row, col), (row + i, col + i)))
                            elif board[row + i][col + i] * turn < 0:
                                moves.append(((row, col), (row + i, col + i)))
                                t1 = False
                            else:
                                t1 = False
                        if row+i <= 7 and col-i >= 0:
                            if board[row + i][col - i] == 0 and t2:
                                moves.append(((row, col), (row + i, col - i)))
                            elif board[row + i][col - i] * turn < 0:
                                moves.append(((row, col), (row + i, col - i)))
                                t2 = False
                            else:
                                t2 = False
                        if row-i >= 0 and col+i <= 7:
                            if board[row - i][col + i] == 0 and t3:
                                moves.append(((row, col), (row - i, col + i)))
                            elif board[row - i][col + i] * turn < 0:
                                moves.append(((row, col), (row - i, col + i)))
                                t3 = False
                            else:
                                t3 = False
                        if row-i >= 0 and col-i >= 0:
                            if board[row - i][col - i] == 0 and t4:
                                moves.append(((row, col), (row - i, col - i)))
                            elif board[row - i][col - i] * turn < 0:
                                moves.append(((row, col), (row - i, col - i)))
                                t4 = False
                            else:
                                t4 = False
    return moves

def generate_rook_moves(board, turn):
    moves = []

    def gen_moves(row, col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            delta_row, delta_col = direction
            next_row, next_col = row + delta_row, col + delta_col

            while 0 <= next_row < 8 and 0 <= next_col < 8:
                target_piece = board[next_row][next_col]

                if target_piece == 0:
                    moves.append(((row, col), (next_row, next_col)))
                elif target_piece * turn < 0:
                    moves.append(((row, col), (next_row, next_col)))
                    break
                else:
                    break

                next_row += delta_row
                next_col += delta_col

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1 and piece == 5:  # White rook
                gen_moves(row, col)
            elif turn == -1 and piece == -5:  # Black rook
                gen_moves(row, col)

    return moves

    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1:
                if piece == 5: # rook
                    gen_moves(board, row, col)
            elif turn == -1:
                if piece == -5:
                    gen_moves(board, row, col)

    return moves

def generate_queen_moves(board, turn):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1:
                if piece == 9:
                    t1 = True
                    t2 = True
                    t3 = True
                    t4 = True
                    t5 = True
                    t6 = True
                    t7 = True
                    t8 = True
                    for i in range(1, 8):
                        if row+i <= 7 and col+i <= 7:
                            if board[row + i][col] <= 0 and t1 == True: # Rook move up
                                moves.append(((row, col), (row + i, col)))
                            else: t1 = False
                            if board[row][col + i] <= 0 and t2 == True: # Rook move right
                                moves.append(((row, col), (row, col + i)))
                            else: t2 = False
                            if board[row + i][col + i] <= 0 and t3 == True: # Bishop move up right
                                moves.append(((row, col), (row + i, col + i)))
                            else: t3 = False
                        if row+i <= 7 and col-i >= 0:
                            if board[row + i][col] <= 0 and t4 == True: # Rook move down
                                moves.append(((row, col), (row + i, col)))
                            else: t4 = False
                            if board[row][col - i] <= 0 and t5 == True: # Rook move left
                                moves.append(((row, col), (row, col - i)))
                            else: t5 = False
                            if board[row + i][col - i] <= 0 and t6 == True: # Bishop move up left
                                moves.append(((row, col), (row + i, col - i)))
                            else: t6 = False
                        if row-i >= 0 and col+i <= 7:
                            if board[row - i][col] <= 0 and t7 == True: # Rook move up
                                moves.append(((row, col), (row - i, col)))
                            else: t7 = False
                            if board[row][col + i] <= 0 and t8 == True: # Rook move right
                                moves.append(((row, col), (row, col + i)))
                            else: t8 = False
                            if board[row - i][col + i] <= 0 and t3 == True: # Bishop move down right
                                moves.append(((row, col), (row - i, col + i)))
                            else: t3 = False
                        if row-i >= 0 and col-i >= 0:
                            if board[row - i][col] <= 0 and t4 == True: # Rook move down
                                moves.append(((row, col), (row - i, col)))
                            else: t4 = False
                            if board[row][col - i] <= 0 and t5 == True: # Rook move left
                                moves.append(((row, col), (row, col - i)))
                            else: t5 = False
                            if board[row - i][col - i] <= 0 and t6 == True: # Bishop move down left
                                moves.append(((row, col), (row - i, col - i)))
                            else: t6 = False
            elif turn == -1:
                if piece == -9:
                    t1 = True
                    t2 = True
                    t3 = True
                    t4 = True
                    t5 = True
                    t6 = True
                    t7 = True
                    t8 = True
                    for i in range(1, 8):
                        if row+i <= 7 and col+i <= 7:
                            if board[row + i][col] >= 0 and t1 == True: # Rook move up
                                moves.append(((row, col), (row + i, col)))
                            else: t1 = False
                            if board[row][col + i] >= 0 and t2 == True: # Rook move right
                                moves.append(((row, col), (row, col + i)))
                            else: t2 = False
                            if board[row + i][col + i] >= 0 and t3 == True: # Bishop move up right
                                moves.append(((row, col), (row + i, col + i)))
                            else: t3 = False
                        if row+i <= 7 and col-i >= 0:
                            if board[row + i][col] >= 0 and t4 == True: # Rook move down
                                moves.append(((row, col), (row + i, col)))
                            else: t4 = False
                            if board[row][col - i] >= 0 and t5 == True: # Rook move left
                                moves.append(((row, col), (row, col - i)))
                            else: t5 = False
                            if board[row + i][col - i] <= 0 and t6 == True: # Bishop move up left
                                moves.append(((row, col), (row + i, col - i)))
                            else: t6 = False
                        if row-i >= 0 and col+i <= 7:
                            if board[row - i][col] >= 0 and t7 == True: # Rook move up
                                moves.append(((row, col), (row - i, col)))
                            else: t7 = False
                            if board[row][col + i] >= 0 and t8 == True: # Rook move right
                                moves.append(((row, col), (row, col + i)))
                            else: t8 = False
                            if board[row - i][col + i] >= 0 and t3 == True: # Bishop move down right
                                moves.append(((row, col), (row - i, col + i)))
                            else: t3 = False
                        if row-i >= 0 and col-i >= 0:
                            if board[row - i][col] >= 0 and t4 == True: # Rook move down
                                moves.append(((row, col), (row - i, col)))
                            else: t4 = False
                            if board[row][col - i] >= 0 and t5 == True: # Rook move left
                                moves.append(((row, col), (row, col - i)))
                            else: t5 = False
                            if board[row - i][col - i] >= 0 and t6 == True: # Bishop move down left
                                moves.append(((row, col), (row - i, col - i)))
                            else: t6 = False

    return moves

def generate_king_moves(board, turn):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == float('inf') * turn:
                # Generate all possible moves for the king
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if row + i >= 0 and row + i < 8 and col + j >= 0 and col + j < 8:
                            target_piece = board[row + i][col + j]
                            if target_piece == 0 or target_piece * turn < 0:
                                moves.append(((row, col), (row + i, col + j)))
    return moves

def generate_all_moves(board, turn):
    moves = []
    
    # Generate moves for pawns
    moves += generate_pawn_moves(board, turn)
    
    # Generate moves for knights
    moves += generate_knight_moves(board, turn)
    
    # Generate moves for bishops
    moves += generate_bishop_moves(board, turn)
    
    # Generate moves for rooks
    moves += generate_rook_moves(board, turn)
    
    # Generate moves for queens
    moves += generate_queen_moves(board, turn)
    
    # Generate moves for king
    moves += generate_king_moves(board, turn)

    if is_king_in_check(board, turn) == True: moves = king_check_moves(board, moves, turn)
    moves = remove_kings_touch_moves(board, moves)
    
    return moves

def is_king_in_check(board, king_color):
    # Find the king's position
    king = float('inf') * king_color
    king_pos = None
    for row in range(8):
        for col in range(8):
            if board[row][col] == king:
                king_pos = (row, col)
                break
        if king_pos:
            break
    
    if not king_pos:
        return False
    
    # Check for attacks from different pieces
    opponent_color = -king_color

    # Check for attacks from pawns
    pawn_moves = generate_pawn_moves(board, opponent_color)
    for move in pawn_moves:
        if move[1] == king_pos:
            return True

    # Check for attacks from knights
    knight_moves = generate_knight_moves(board, opponent_color)
    for move in knight_moves:
        if move[1] == king_pos:
            return True

    # Check for attacks from bishops or queens (diagonal attacks)
    diagonal_moves = generate_bishop_moves(board, opponent_color)
    for move in diagonal_moves:
        if move[1] == king_pos:
            return True

    # Check for attacks from rooks or queens (straight attacks)
    straight_moves = generate_rook_moves(board, opponent_color)
    for move in straight_moves:
        if move[1] == king_pos:
            return True

    straight_moves = generate_queen_moves(board, opponent_color)
    for move in straight_moves:
        if move[1] == king_pos:
            return True
        
    straight_moves = generate_king_moves(board, opponent_color)
    for move in straight_moves:
        if move[1] == king_pos:
            return True

    return False

def king_check_moves(board, moves, king_color):
    valid_moves = []

    for move in moves:
        new_board = copy.deepcopy(board)
        start_pos, end_pos = move

        # Perform the move on the new board
        new_board[end_pos[0]][end_pos[1]] = new_board[start_pos[0]][start_pos[1]]
        new_board[start_pos[0]][start_pos[1]] = 0

        if not is_king_in_check(new_board, king_color):
            valid_moves.append(move)

    if not valid_moves:
        print(f'Checkmate, {king_color*-1} Wins!')
        sys.exit()

    return valid_moves

def remove_kings_touch_moves(board, moves):
    new_moves = []
    
    for move in moves:
        
        start_pos, end_pos = move
        start_piece = board[start_pos[0]][start_pos[1]]
        end_piece = board[end_pos[0]][end_pos[1]]
        
        # Create a temporary board to simulate the move
        temp_board = copy.deepcopy(board)
        temp_board[end_pos[0]][end_pos[1]] = start_piece
        temp_board[start_pos[0]][start_pos[1]] = 0
        
        # Find the positions of both kings
        white_king_pos = None
        black_king_pos = None
        for row in range(8):
            for col in range(8):
                if temp_board[row][col] == float('inf'):
                    white_king_pos = (row, col)
                elif temp_board[row][col] == float('-inf'):
                    black_king_pos = (row, col)
        
        # Check if the kings are adjacent
        if white_king_pos and black_king_pos and are_adjacent(white_king_pos, black_king_pos):
            continue  # Skip the move if it leads to kings touching each other
        
        new_moves.append(move)
    
    return new_moves


def are_adjacent(pos1, pos2):
    row_diff = abs(pos1[0] - pos2[0])
    col_diff = abs(pos1[1] - pos2[1])
    return row_diff <= 1 and col_diff <= 1

# Now that our piece movement works, let's check if a piece of the other color is captured
# We want to not only return true BUT we want to return what that piece was & in turn it's point value

def is_captured(board, side, y, x):
    piece = board[y][x]
    if side == 1 and piece < 0:
        return abs(piece) # Convert to absolute value - might change this later
    elif side == -1 and piece > 0:
        return abs(piece)
    else:
        return 0

# let's adjust our method for VALIDATING user moves to simply adding them to an array and generating ALL possible moves

# Now detect checkmate

def is_checkmate(board, side):
    if not is_king_in_check(board, side):
        return False

    moves = generate_all_moves(board, side)

    if len(moves) == 0:
        return True

    for move in moves:
        start_row, start_col = move[0][0], move[0][1]
        end_row, end_col = move[1][0], move[1][1]
        captured_piece = is_captured(board, side, end_row, end_col)

        hypothetical_board = copy.deepcopy(board)
        hypothetical_board[end_row][end_col] = hypothetical_board[start_row][start_col]
        hypothetical_board[start_row][start_col] = 0

        if is_king_in_check(hypothetical_board, side):
            continue

        return False

    return True

TURN = -1

def is_draw(board):
    # Check for lack of material
    piece_counts = {}
    for row in board:
        for piece in row:
            if piece != 0:
                piece_counts[piece] = piece_counts.get(piece, 0) + 1
    
    # Determine if there is insufficient material for a checkmate
    if (
        len(piece_counts) == 2 and
        all(count == 1 or count == 2 for count in piece_counts.values())
    ):
        return True
    
    # Check for stalemate
    if not generate_all_moves(board, 1) and not is_king_in_check(board, 1):
        return True
    
    return False

def pawn_promotion(board):
    # Promote pawns on the 0th row to a queen (-1 to -9)
    for col in range(8):
        if board[0][col] == -1:
            board[0][col] = -9

    # Promote pawns on the 7th row to a queen (1 to 9)
    for col in range(8):
        if board[7][col] == 1:
            board[7][col] = 9

    return board

def move_piece(board, y, x, newy, newx):
    board[newy][newx] = board[y][x]
    board[y][x] = 0
    return board


#while True:

'''board = create_board()
moves = generate_all_moves(board, TURN)
'''
'''for i in range(len(moves)):
    move = moves[i]
    capture = is_captured(board, TURN, move[1][0], move[1][1])
    moves[i] = (capture,) + move

    if is_checkmate(board, TURN):
        if TURN == -1:
            print('WHITE WINS')
        elif TURN == 1:
            print('BLACK WINS')

TURN *= -1'''

''' 
board = [
    [5, 3, 3.5, 9, float('inf'), 3.5, 3, 5],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-1, -1, -1, -1, -1, -1, -1, -1],
    [-5, -3, -3.5, -9, float('-inf'), -3.5, -3, -5]]    
'''


board = [
    [0, 0, 0, 0, float('inf'), 0, 0, -5],
    [0, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, float('-inf'), 0, 0, 0]]    