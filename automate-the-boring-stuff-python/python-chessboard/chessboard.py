import sys, copy

STARTING_PIECES = {'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR', 'a7': 'bP', 'b7': 'bP',
'c7': 'bP', 'd7': 'bP', 'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ', 'e1': 'wK', 'f1': 'wB',
'g1': 'wN', 'h1': 'wR', 'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'}

BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
WHITE_SQUARE = '||'
BLACK_SQUARE = '  '


def print_chess_board(board):
    squares = []
    is_white_square = True
    for y in '87654321':
        for x in 'abcdefgh':
            #print(x, y, is_white_square)  # DEBUG: Shows coordinates in order.
            if x + y in board.keys():
              squares.append(board[x + y])
            else:
              if is_white_square:
                squares.append(WHITE_SQUARE)
              else:
                squares.append(BLACK_SQUARE)
            is_white_square = not is_white_square
        is_white_square = not is_white_square

    print(BOARD_TEMPLATE.format(*squares))

def print_help():
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  validate - Validate the pieces and position on the board meet chess rules')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')

#*
# Has one black king
# Has one white king
# Each player can have at most 16 pieces
# 8/16 are pawns
# All pieces must be in bounds
# Pieces begin with w or b to represent their color
# 
# *#


# def validate_board(board):
#     count = {}
#     total_white = 0
#     total_black = 0
#     valid_piece_types = {'P', 'N', 'B', 'R', 'Q', 'K'}

#     for position, piece in board.items():
#         if piece[0] != 'b' and piece[0] != 'w':
#             print(f"Piece on {position} has to be either black or white")
#             return f"Piece on {position} has to be either black or white"
#         if piece[1] not in valid_piece_types:
#             print(f"Invalid piece located in {position}")
#             return f"Invalid piece located in {position}"
#         if position[0] not in 'abcdefgh' or position[1] not in '87654321':
#             print(f"Pieces need to be within the bounds of the board")
#             return "Pieces need to be within the bounds of the board"
#         if piece not in count:
#             count.setdefault(piece, 1)
#         else:
#             count[piece] += 1
#         if piece[0] == 'b':
#             total_black += 1
#         elif piece[0] == 'w':
#             total_white += 1
    
#     if (total_white == 16 and total_black == 16) and (count['wK'] == 1 and count['bK'] == 1) and (count['wP'] == 8 and count['bP'] == 8):
#         print("Your board satifies all criteria.")

def validate_board(board):
    count = {}
    total_white = 0
    total_black = 0
    valid_piece_types = {'P', 'N', 'B', 'R', 'Q', 'K'}
    errors = []

    for position, piece in board.items():
        if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
            errors.append(f"Invalid board position: {position}")
        if len(piece) != 2 or piece[0] not in 'bw' or piece[1] not in valid_piece_types:
            errors.append(f"Invalid piece: {piece} at {position}")
        count[piece] = count.get(piece, 0) + 1
        if piece[0] == 'b':
            total_black += 1
        elif piece[0] == 'w':
            total_white += 1

    if count.get('wK', 0) != 1:
        errors.append("There must be exactly one white king.")
    if count.get('bK', 0) != 1:
        errors.append("There must be exactly one black king.")
    if total_white > 16:
        errors.append(f"Too many white pieces: {total_white}")
    if total_black > 16:
        errors.append(f"Too many black pieces: {total_black}")
    if count.get('wP', 0) > 8:
        errors.append(f"Too many white pawns: {count.get('wP', 0)}")
    if count.get('bP', 0) > 8:
        errors.append(f"Too many black pawns: {count.get('bP', 0)}")

    if errors:
        for error in errors:
            print("Error:", error)
        return 1
    else:
        print("Board is valid and satisfies all criteria.")
        return 0

main_board = copy.copy(STARTING_PIECES)
print_help()
while True:
    print_chess_board(main_board)
    response = input('> ').split()

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]
    elif response[0] == 'remove':
        del main_board[response[1]]
    elif response[0] == 'set':
        main_board[response[1]] = response[2]
    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)
    elif response[0] == 'clear':
        main_board = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]
    elif response[0] == 'validate':
        validate_board(main_board)
    elif response[0] == 'help':
        print_help()
    elif response[0] == 'quit':
        sys.exit()
