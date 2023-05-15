def create_board():
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

def generate_pawn_moves(board):
    moves = []
    
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 1:  # white pawn
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
                    
            elif piece == -1:  # black pawn
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

def generate_knight_moves(board):
    moves = []

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 3: # then it's a knight

                # Check all possible L-shaped moves
                for i, j in [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1), 
                             (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]:

                    # Only consider moves that are within the bounds of the board
                    if i >= 0 and i < 8 and j >= 0 and j < 8:
                        if board[i][j] == 0: # In the future we can do <= and the opposite for the other side
                            moves.append(((row, col), (i, j)))

    return moves

def generate_bishop_moves(board):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 3.5:
                t1 = True
                t2 = True
                t3 = True
                t4 = True
                for i in range(1, 8):
                    if row+i <= 7 and col+i <= 7:
                        if board[row + i][col + i] == 0 and t1 == True: # In the future we can do <= and the opposite for the other side
                            moves.append(((row, col), (row + i, col + i)))
                        else: t1 = False
                    if row+i <= 7 and col-i >= 0:
                        if board[row + i][col - i] == 0 and t2 == True:
                            moves.append(((row, col), (row + i, col - i)))
                        else: t2 = False
                    if row-i >= 0 and col+i <= 7:
                        if board[row - i][col + i] == 0 and t3 == True:
                            moves.append(((row, col), (row - i, col + i)))
                        else: t3 = False
                    if row-i >= 0 and col-i >= 0:
                        if board[row - i][col - i] == 0 and t4 == True:
                            moves.append(((row, col), (row - i, col - i)))
                        else: t4 = False
    return moves


def generate_rook_moves(board):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 5: # rook
                for i in range(1, 8):
                    # check moves in vertical direction
                    if row+i <= 7 and board[row+i][col] == 0:
                        moves.append(((row, col), (row+i, col)))
                    else:
                        break
                    # check moves in horizontal direction
                    if col+i <= 7 and board[row][col+i] == 0:
                        moves.append(((row, col), (row, col+i)))
                    else:
                        break
                    if row-i >= 0 and board[row-i][col] == 0:
                        moves.append(((row, col), (row-i, col)))
                    else:
                        break
                    if col-i >= 0 and board[row][col-i] == 0:
                        moves.append(((row, col), (row, col-i)))
                    else:
                        break
    return moves

def generate_queen_moves(board):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
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
                        if board[row + i][col] == 0 and t1 == True: # Rook move up
                            moves.append(((row, col), (row + i, col)))
                        else: t1 = False
                        if board[row][col + i] == 0 and t2 == True: # Rook move right
                            moves.append(((row, col), (row, col + i)))
                        else: t2 = False
                        if board[row + i][col + i] == 0 and t3 == True: # Bishop move up right
                            moves.append(((row, col), (row + i, col + i)))
                        else: t3 = False
                    if row+i <= 7 and col-i >= 0:
                        if board[row + i][col] == 0 and t4 == True: # Rook move down
                            moves.append(((row, col), (row + i, col)))
                        else: t4 = False
                        if board[row][col - i] == 0 and t5 == True: # Rook move left
                            moves.append(((row, col), (row, col - i)))
                        else: t5 = False
                        if board[row + i][col - i] == 0 and t6 == True: # Bishop move up left
                            moves.append(((row, col), (row + i, col - i)))
                        else: t6 = False
                    if row-i >= 0 and col+i <= 7:
                        if board[row - i][col] == 0 and t7 == True: # Rook move up
                            moves.append(((row, col), (row - i, col)))
                        else: t7 = False
                        if board[row][col + i] == 0 and t8 == True: # Rook move right
                            moves.append(((row, col), (row, col + i)))
                        else: t8 = False
                        if board[row - i][col + i] == 0 and t3 == True: # Bishop move down right
                            moves.append(((row, col), (row - i, col + i)))
                        else: t3 = False
                    if row-i >= 0 and col-i >= 0:
                        if board[row - i][col] == 0 and t4 == True: # Rook move down
                            moves.append(((row, col), (row - i, col)))
                        else: t4 = False
                        if board[row][col - i] == 0 and t5 == True: # Rook move left
                            moves.append(((row, col), (row, col - i)))
                        else: t5 = False
                        if board[row - i][col - i] == 0 and t6 == True: # Bishop move down left
                            moves.append(((row, col), (row - i, col - i)))
                        else: t6 = False
    return moves

def generate_king_moves(board):
    moves = []
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece == 6:
                # Generate all possible moves for the king
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        if row + i >= 0 and row + i < 8 and col + j >= 0 and col + j < 8:
                            if board[row + i][col + j] == 0 or board[row + i][col + j] % 2 != piece % 2:
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
print(generate_all_moves(board))
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