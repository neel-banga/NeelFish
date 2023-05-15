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

    return board

def is_captured(board, piece, y, x): # Taking in new positions
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
            if piece == 1 and turn == 1:  
                if row == 1:
                    if board[row+1][col] == 0 and board[row+2][col] == 0:
                        moves.append(((row, col), (row+2, col)))
                if row < 7 and board[row+1][col] == 0:
                    moves.append(((row, col), (row+1, col)))
                if row < 7 and col < 7 and board[row+1][col+1] < 0: 
                    moves.append(((row, col), (row+1, col+1)))
                if row < 7 and col > 0 and board[row+1][col-1] < 0:
                    moves.append(((row, col), (row+1, col-1)))
                    
            elif piece == -1 and turn == -1:  
                if row == 6:
                    if board[row-1][col] == 0 and board[row-2][col] == 0:
                        moves.append(((row, col), (row-2, col)))
                if row > 0 and board[row-1][col] == 0:
                    moves.append(((row, col), (row-1, col)))
                if row > 0 and col < 7 and board[row-1][col+1] > 0:
                    moves.append(((row, col), (row-1, col+1)))
                if row > 0 and col > 0 and board[row-1][col-1] > 0:
                    moves.append(((row, col), (row-1, col-1)))
                    
    return moves

def generate_knight_moves(board, turn):
    moves = []

    def gen_moves(row, col, board):
        for i, j in [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1), 
                    (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]:

            if i >= 0 and i < 8 and j >= 0 and j < 8:
                if board[i][j] == 0 or board[i][j] * turn < 0:
                    moves.append(((row, col), (i, j)))

    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if turn == 1:
                if piece == 3:
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