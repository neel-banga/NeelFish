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


# Create all combos with old board and then check it in terms of new board

def check_pawn():

def check_knight():

def check_bishop():

def check_rook():

def check_queen():


def check_user_move(board, piece, x, y):

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

    elif piece == 3: # knight

    elif piece == 3.5: # bishop
    
    elif piece == 5: # rook

    elif piece == 9: # queen

    else: # king


    # Here let's check if that value of y,x has a piece (meaning it has to be of the other side)
    # We have to do something with that value