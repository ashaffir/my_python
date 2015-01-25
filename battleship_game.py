from random import randint

board = []
twod_board = []

for i in range(0,5):
    for j in range(0,5):
        twod_board.append("O")
    board.append(twod_board)
    twod_board = []

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    row_idnx = randint(0, len(board) - 1)
    return row_idnx

def random_col(board):
    col_idnx = randint(0, len(board) - 1)
    return col_idnx

ship_row = random_row(board)
ship_col = random_col(board)

print "Ship Col = %i" % ship_col
print "Ship Row = %i" % ship_row

for turn in range(4):
    tmp = turn + 1
    print "Turn %s" % tmp
    #Input guess from player
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    # Check the guess
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        print "Game Over"
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean."
            print "Game Over"
        elif board[guess_row][guess_col] == "X":
            print  "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
            if tmp == 3:
                print "Game Over"

