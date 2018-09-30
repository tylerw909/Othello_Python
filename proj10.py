###############################################################################
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#TylerWeisner
#                           PROJECT 10
#                           April 17, 2018
'''                         
This code is our first game using Python.  It simulates the game of Reversi or
Othello.  Where we use a class created for the game and use it to write the 
working game.  You have to scan over the board object and each spot and flip 
the game pieces according to the rules and whoever has more pieces captured 
when the board is full, either black or white wins. 
'''
###############################################################################
import reversi
import string
LETTERS = string.ascii_lowercase

def indexify(position):
    """
    Indexify takes a position like "A4" and translates it into point 
    coordinate and returns it.
    """

    letter = int( LETTERS.find( position[:1] ) )
    number = int( position[1:] )
    
    pt = ( letter , number - 1)
    
    return(pt)
    
    

def deindexify(row, col):
    """
    Takes a point on the board (row , column) and turns it back into a board
    letter index like "A4".
    """
    letter = str( LETTERS[row] )
    number = str( col + 1)
    position = letter + number
    
    return position
    


def initialize(board):
    """
    Initializes the game by setting up the starting position with two black 
    and two white pieces crossed in the middle.
    """
    length = board.length
    row = int( length/2 ) - 1
    col = int( length/2 ) - 1
    
    white1 = reversi.Piece('white')
    white2 = reversi.Piece('white')
    black1 = reversi.Piece('black')
    black2 = reversi.Piece('black')
    
    board.place( row, col, white1)
    board.place( row, col +1, black1)
    board.place( row +1, col +1, white2)
    board.place( row +1, col, black2)
    
    
    
def count_pieces(board):
    """
    Counts the total number of black and white pieces on the board.
    """
    black_count = 0
    white_count = 0
    
    for r in board.cell:
        
        for c in r: 
            
            if c == None:
                continue
            
            if c.is_black():
                black_count += 1
            
            elif c.is_white():
                white_count += 1
            
    color_count = (black_count , white_count)
    
    return color_count
        


def get_all_streaks(board, row, col, piece_arg):
    """
    It takes a place on the board and returns a dictionary with the 8 
    directions east, west, north-east, etc. and the pieces that would be 
    captured in the 8 directions as the values.
    """
    streaks = {'e': None, 'w': None, 'n': None, 's': None, \
               'ne': None, 'nw': None, 'se': None, 'sw': None}
    
    color = piece_arg.color()
    other_color = 'white' if color == 'black' else 'black'
    # north
    L = []
    c = col
    for r in range(row-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['n'] = sorted(L)

#    # east
    L = []
    c = col
    r = row
    for c in range(col+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['e'] = sorted(L)
 
#    # south
    L = []
    c = col
    r = row
    for r in range(row+1,board.length):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['s'] = sorted(L)

#    # west
    L = []
    c = col
    r = row
    for c in range(col-1,-1,-1):
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
    else:
        L = [] # streak not terminated with color piece
    streaks['w'] = sorted(L)

#    # northeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row-1,-1,-1):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['ne'] = sorted(L)
        
#    # southeast
    L = []
    c = col
    r = row
    c = col+1
    for r in range(row+1,board.length):
        if c == board.length:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c += 1
    else:
        L = [] # streak not terminated with color piece
    streaks['se'] = sorted(L)
                
#    # southwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row+1,board.length):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['sw'] = sorted(L)
    
#    # northwest
    L = []
    c = col
    r = row
    c = col - 1
    for r in range(row-1,-1,-1):
        if c == -1:
            L = []  # terminated without finding color
            break
        if not board.is_free(r,c):
            piece = board.get(r,c)
            if piece.color() == other_color:
                L.append((r,c))
            else:
                break # terminated streak with color
        else:
            L = []  # terminated without finding color
            break
        c = c - 1
    else:
        L = [] # streak not terminated with color piece
    streaks['nw'] = sorted(L)
            
    return streaks



def get_all_capturing_cells(board, piece):
    """
    Basically, this function calls the get_all_streaks() function on each 
    empty cell on the current board, and builds a dictionary by using the 
    (row, col) tuple as the key and the sorted list of cells that it can 
    capture from all the directions returned by the get_all_streaks() function.
    """
    D = {}
    
    for row in range(board.length): #whole row
        
        for col in range(board.length): #all column first
            if board.is_free(row , col):
                
                streaks = get_all_streaks( board , row , col , piece ) #streaks
                
                for k,v in streaks.items(): #iterates dicionary of points
                    
                    if v != []:
                        temp_list = sorted(v) #sorted list of capturable cells
                        
                        if (row, col) in D :
                            D[(row, col)].extend(temp_list)
                        
                        else:
                            D[(row, col)] = temp_list
        
    for k,v in D.items():
        v.sort()
        
    return D
                
        


def get_hint(board, piece):
    """
    Helps the user decide what moves are available based on the amount of 
    capturable pieces in directions.
    """
    
    captures = get_all_capturing_cells(board , piece)
    hint_list = []
    
    for k,v in captures.items(): #k is tuple of rows and cols
        result = len(v)
        hint_list.append( [result , k] )
        
    hint_list.sort( reverse = True )
    
    temp_list = []
    
    for i in hint_list:
        
        temp_list.append( deindexify(i[1][0] , i[1][1]) ) 
        #adds board points to the temp_list
        
        
    return temp_list


    
def place_and_flip(board, row, col, piece):
    """
    Allows players to place a their next piece based on a row and column 
    coordinate.  Also prevents errors for an already occupied space, 
    not capturable space, and any invalid positions.
    """
    
    color = str(piece)
    dex = deindexify(row,col)
    try:
        if board.get(row , col):
            raise ValueError()("Can't place {:s} at '{:s}',".format(color,dex)\
            +"already occupied. Type 'hint' to get suggestions")
            
        streaks = get_all_streaks(board, row, col, piece)
        temp_list =[]
        
        for k,v in streaks.items():
            
            if v: #if there is an open spot
                temp_list.extend(v)
                
        if temp_list:#is it empty or not
            board.place(row , col , piece)
            
            for position in temp_list: # if EVERYTHING is good, then flip 
                    board.get( position [0] , position[1] ).flip()
        
        else:
            raise ValueError("Can't place {:s} at '{:s}',".format(color,dex)\
                +" it's not a capture. Type 'hint' to get suggestions.")
        
    except IndexError:
        raise ValueError("Can't place {:s} at '{:s}',".format(color,dex)\
                         +"invalid position. Type 'hint' to get suggestions.")
            
    


def is_game_finished(board):
    """
    Function checks if the game is finished by checking to see if the board
    is full or not.
    """
    white = get_all_capturing_cells(board , reversi.Piece("white"))
    black = get_all_capturing_cells(board , reversi.Piece("black"))
    
    return board.is_full() or len(white) == 0 and len(black) == 0 

      

      
def get_winner(board):
    """
    Uses count_pieces to compare the amount of black pieces to the whites and
    whichever is greater wins!
    """
    num_black = count_pieces(board)[0] #counts total black pieces
    num_white = count_pieces(board)[1]
    winner = ''
    
    if num_black == num_white:
        winner = "draw"
    
    elif num_black > num_white:
        winner = "black"
        
    else:
        winner = "white"
        
    return winner


def choose_color():
    """
    Asks for input from player one for color. Gives other color to the second
    player. Doesn't let the input be invalid otherwise reprompts. Returns
    player's colors.
    """
    player1 = input("Pick a color: ")
    player2 = ''
    
    #reprompts if the player doesn't give valid color
    while player1 != 'black' and player1 != 'white':
        print("Wrong color, type only 'black' or 'white', try again.")
        player1 = input("Pick a color: ")
        
    if player1 == 'black':
        player2 = 'white'
        
    else:
        player2 = 'black'
    
    print("You are '{:s}' and your opponent is '{:s}'."\
          .format(player1,player2))
    
    return (player1, player2)



def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    """
    
    banner = """
     _____                         _ 
    |  __ \                       (_)
    | |__) |_____   _____ _ __ ___ _ 
    |  _  // _ \ \ / / _ \ '__/ __| |
    | | \ \  __/\ V /  __/ |  \__ \ |
    |_|  \_\___| \_/ \___|_|  |___/_|
    
    Developed by The Students Inc.
    CSE231 Spring Semester 2018
    Michigan State University
    East Lansing, MI 48824, USA.
    """

    prompt = "[{:s}'s turn] :> "
    print(banner)
   
    # Choose the color here
    (my_color, opponent_color) = choose_color()
    
    # Take a board of size 8x8
    # Prompt for board size
    size = input("Input a board size: ")
    board = reversi.Board(int(size))
    initialize(board)
    
    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'white' else opponent_color
    
    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)
            
            print("Current board:")
            board.display(piece_count)    
            
            # Get a piece according to turn
            piece = reversi.Piece(turn)

            # Get the command from user using input
            command = input(prompt.format(turn)).lower()
            
            # Now decide on different commands
            if command == 'exit':
                break
            elif command == 'hint':
                print("\tHint: " + ", ".join(get_hint(board, piece)))
            elif command == 'pass':
                hint = get_hint(board, piece)
                if len(hint) == 0:
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
                    print("\tHanded over to \'{:s}\'.".format(turn))
                else:
                    print("\tCan't hand over to opponent, you have moves," + \
                          " type \'hint\'.")
            else:
                    (row, col) = indexify(command)
                    place_and_flip(board, row, col, piece)
                    print("\t{:s} played {:s}.".format(turn, command))
                    turn = my_color if turn == opponent_color \
                                        else opponent_color
        except Exception as err:
            print("Error:", err)
    
    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)    
    winner = get_winner(board)
    if winner != 'draw':
        diff = abs(piece_count[0] - piece_count[1])
        print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
    else:
        print("This game ends in a draw.")
    # --- end of game play ---



def figure_1(board):
    """
    You can use this function to test your program
    """
    board.place(0,0,reversi.Piece('black'))
    board.place(0,3,reversi.Piece('black'))
    board.place(0,4,reversi.Piece('white'))
    board.place(0,5,reversi.Piece('white'))
    board.place(0,6,reversi.Piece('white'))
    board.place(1,1,reversi.Piece('white'))
    board.place(1,3,reversi.Piece('white'))
    board.place(1,5,reversi.Piece('white'))
    board.place(1,6,reversi.Piece('white'))
    board.place(1,7,reversi.Piece('white'))
    board.place(2,2,reversi.Piece('white'))
    board.place(2,3,reversi.Piece('black'))
    board.place(2,4,reversi.Piece('white'))
    board.place(2,5,reversi.Piece('white'))
    board.place(2,7,reversi.Piece('white'))
    board.place(3,0,reversi.Piece('black'))
    board.place(3,1,reversi.Piece('white'))
    board.place(3,2,reversi.Piece('white'))
    board.place(3,4,reversi.Piece('white'))
    board.place(3,5,reversi.Piece('white'))
    board.place(3,6,reversi.Piece('black'))
    board.place(3,7,reversi.Piece('black'))
    board.place(4,0,reversi.Piece('white'))
    board.place(4,2,reversi.Piece('white'))
    board.place(4,4,reversi.Piece('white'))
    board.place(5,0,reversi.Piece('black'))
    board.place(5,2,reversi.Piece('black'))
    board.place(5,3,reversi.Piece('white'))
    board.place(5,5,reversi.Piece('black'))
    board.place(6,0,reversi.Piece('black'))
    board.place(6,1,reversi.Piece('black'))
    board.place(6,3,reversi.Piece('white'))
    board.place(6,6,reversi.Piece('white'))
    board.place(7,1,reversi.Piece('black'))
    board.place(7,2,reversi.Piece('white'))
    board.place(7,3,reversi.Piece('black'))
    board.place(7,7,reversi.Piece('black'))
    
if __name__ == "__main__":
    game_play_human()
