from game import board

print("Would you like to go first? 'y' for yes and 'n' for no")
firstTurn = None
while True:
    firstTurn = input()
    if firstTurn == "y" or firstTurn == "n":
        break
    print("Invalid input, please enter 'y' or 'n' (without the ')")

board = board()
if firstTurn == "y":
    humanPiece = 'r'
    aiPiece = 'b'
    board.print()
    print("Select a number associated with the column you want to choose")
    while True:
        column = input()
        if board.isValidColumn(column):
            board.addPiece(humanPiece, column)
            break
else:
    humanPiece = 'b'
    aiPiece = 'r'
# Computer moves, then...
while board.winner is None and not board.isFull():
    board.print()
    print("Select a number associated with the column you want to choose")
    while True:
        column = input()
        if board.isValidColumn(column):
            if board.addPiece(humanPiece, column):
                print("You win!")
            break
    if board.winner is not None or board.isFull():
        break
    # Computer moves
board.print()
