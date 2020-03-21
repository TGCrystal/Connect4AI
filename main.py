from game import board

print("Would you like to go first? 'y' for yes and 'n' for no")
firstTurn = None
while True:
    firstTurn = input()
    if firstTurn == "y" or firstTurn == "n":
        break
    print("Invalid input, please enter 'y' or 'n' (without the ')")

board = board()
board.print()
while firstTurn == "y":
    print("Select a number associated with the column you want to choose")
    column = input()
    if board.isValidColumn(column):
        board.addPiece('r', column)
# Computer moves, then...
board.print()

