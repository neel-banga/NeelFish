'''

Buggy parts to fix

- fix spot_taken function
- fix the easy IF statements (whether it is in bounds or not)
- check every other peice 
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
        
        # Now let's check for en passant
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

            if old_x == x and old_y + i == y:
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
    '''
    if not x <= 7 and not x >= 0:
        return False

    if piece >= 0:

        if board[y][x] >= 0:

            return False

    if piece <= 0:

        if board[y][x] <= 0:

            return False
    ''' 

    # Now that our piece movement works, let's check if a piece of the other color is captured
    # We want to not only return true BUT we want to return what that piece was & in turn it's point value

    def is_captured():
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
    
    # Here let's check if that value of y,x has a piece (meaning it has to be of the other side)
    # We have to do something with that value

    captured = is_captured()

    # Here if there is no piece captured we can just return True or maybe 0??
    if captured == False:
        return True
    
    # if there is though, let's just return that value

    else:
        return captured
    
board = create_board()
print(check_user_move(board, 5, 0, 7, 3, 8))
print(board[0][7])


# Just to make my life easy

# def check_user_move(board, piece, old_x, old_y, x, y):

#print(board[]) - debugging, not exactly working!