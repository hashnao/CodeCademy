from random import randint

board = []

for i in range(5):
    board.append(["O"]*5)

def print_board(board):
    for row in board:
      print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
print ship_col
print ship_row
