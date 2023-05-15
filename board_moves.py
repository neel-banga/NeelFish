'''

Buggy parts to fix

- fix the easy IF statements (whether it is in bounds or not)
- also make sure that rook and bishop can't just IGNORE the pawn in front of it lol


'''



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
                if board[i][j] == 0 or board[row][col+i] * turn < 0:
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
    def gen_moves(board, row, col):
        for i in range(1, 8):
            # check moves in vertical direction
            if row+i <= 7:
                if board[row+i][col] == 0 or board[row+i][col] * turn < 0:
                    moves.append(((row, col), (row+i, col)))
                if board[row+i][col] != 0:
                    break

            # check moves in horizontal direction
            if col+i <= 7:
                if board[row][col+i] == 0 or board[row][col+i] * turn < 0:
                    moves.append(((row, col), (row, col+i)))
                if board[row][col+i] != 0:
                    break

            if row-i >= 0:
                if board[row-i][col] == 0 or board[row-i][col] * turn < 0:
                    moves.append(((row, col), (row-i, col)))
                if board[row-i][col] != 0:
                    break

            if col-i >= 0:
                if board[row][col-i] == 0 or board[row][col-i] * turn < 0:
                    moves.append(((row, col), (row, col-i)))
                if board[row][col-i] != 0:
                    break

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

def generate_king_moves(board):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == float('inf'):
                # Generate all possible moves for the king
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if row + i >= 0 and row + i < 8 and col + j >= 0 and col + j < 8:
                            if board[row + i][col + j] == 0 or board[row + i][col + j] * piece < 0:
                                moves.append(((row, col), (row + i, col + j)))
    return moves

def generate_all_moves(board):
    moves = []
    
    # Generate moves for pawns
    moves += generate_pawn_moves(board)
    
    # Generate moves for knights
    moves += generate_knight_moves(board)
    
    # Generate moves for bishops
    moves += generate_bishop_moves(board)
    
    # Generate moves for rooks
    moves += generate_rook_moves(board)
    
    # Generate moves for queens
    moves += generate_queen_moves(board)
    
    # Generate moves for king
    moves += generate_king_moves(board)
    
    return moves


def is_king_in_check(board, king_color):
    # Find the king's position
    king_pos = None
    for row in range(8):
        for col in range(8):
            if board[row][col] == king_color * 6:
                king_pos = (row, col)
                break
        if king_pos:
            break
    
    if not king_pos:
        return False
    
    # Check for attacks on the king's position
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != 0 and piece // abs(piece) != king_color:
                if (row, col) in generate_all_moves(board, row, col):
                    return True
    
    return False

# let's adjust our method for VALIDATING user moves to simply adding them to an array and generating ALL possible moves

board = create_board()
print(generate_queen_moves(board, -1))
print(is_king_in_check(board, -1))


# Just to make my life easy

# def check_user_move(board, piece, old_y, old_x, y, x):

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

# In the future we can do <= and the opposite for the other side