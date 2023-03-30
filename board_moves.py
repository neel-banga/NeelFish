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

def check_user_move(board, piece, old_x, old_y, x, y):

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
        
        # Now let's check for en passant
        if (old_x + 1 == x and old_y + 1 == y) or (old_x - 1 == x and old_y + 1 == y):
            # let's make sure a peice of the opposite color is on that position
            if new_board[y][x]:
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

        for i in range(1, 8):

            if spot_taken() == False:
                return False

            if old_x + i == x and old_y + i == y:
                return True
            
        return False

    def check_rook():

        if spot_taken() == False:
            return False

        for i in range(1, 8):
            if old_x + i == x and old_y == y:
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

    if not x <= 7 and not x >= 0:
        return False

    if piece >= 0:

        if board[y][x] >= 0:

            return False

    if piece <= 0:

        if board[y][x] <= 0:

            return False
    

    # We use an index slice in order to make sure that the array isn't linked to the same memory adress
    new_board = board[:]    

    new_board[y][x] = piece

    if piece == 1: # pawn
        check_pawn(board, new_board)

    elif piece == 3: # knight
        check_knight(board, new_board)

    elif piece == 3.5: # bishop
        check_bishop(board, new_board)
    
    elif piece == 5: # rook
        check_rook(board, new_board)

    elif piece == 9: # queen
        check_queen(board, new_board)

    else:
        check_king(board, new_board)
    
    return True

    # Here let's check if that value of y,x has a piece (meaning it has to be of the other side)
    # We have to do something with that value