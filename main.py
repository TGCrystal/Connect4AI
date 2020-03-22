import os
import sys


# Enable and disable print from https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def minAI(gameBoard, aiPiece, alpha=float('-inf'), beta=float('inf')):
    if aiPiece == 'r':
        humanPiece = 'b'
    else:
        humanPiece = 'r'
    if gameBoard.isFull():
        return 0, None
    bestScore = 0
    bestAction = None
    actions = gameBoard.getValidMoves()
    for action in actions:
        isWin, row = gameBoard.addPiece(humanPiece, action)
        gameBoard.resetPosition(row, action)
        if isWin:
            return -1, action
    for action in actions:
        row = gameBoard.addPiece(humanPiece, action)[1]
        successorScore = maxAI(gameBoard, aiPiece, alpha, beta)[0]
        gameBoard.resetPosition(row, action)  # gameBoard isn't deep copied, so must be preserved
        if bestAction is None or successorScore < bestScore:
            if successorScore < beta:
                beta = successorScore
            bestScore = successorScore
            bestAction = action
            if alpha > beta:
                return bestScore, bestAction
    if bestAction is None:  # "if" at start of method should ensure this doesn't happen
        return 0, None
    return bestScore, bestAction


def maxAI(gameBoard, aiPiece, alpha=float('-inf'), beta=float('inf')):
    if gameBoard.isFull():
        return 0, None
    bestScore = 0
    bestAction = None
    actions = gameBoard.getValidMoves()
    for action in actions:
        isWin, row = gameBoard.addPiece(aiPiece, action)
        gameBoard.resetPosition(row, action)
        if isWin:
            return 1, action
    for action in actions:
        row = gameBoard.addPiece(aiPiece, action)[1]
        successorScore = minAI(gameBoard, aiPiece, alpha, beta)[0]
        gameBoard.resetPosition(row, action)  # gameBoard isn't deep copied, so must be preserved
        if bestAction is None or successorScore > bestScore:
            if successorScore > alpha:
                alpha = successorScore
            bestScore = successorScore
            bestAction = action
            if alpha > beta:
                return bestScore, bestAction
    if bestAction is None:  # "if" at start of method should ensure this doesn't happen
        return 0, None
    return bestScore, bestAction


def main():
    from game import board
    print("Would you like to go first? 'y' for yes and 'n' for no")
    firstTurn = None
    while True:
        firstTurn = input()
        if firstTurn == "y" or firstTurn == "n":
            break
        print("Invalid input, please enter 'y' or 'n' (without the ')")

    gameBoard = board()
    if firstTurn == "y":
        humanPiece = 'r'
        aiPiece = 'b'
        gameBoard.print()
        print("Select a number associated with the column you want to choose")
        while True:
            column = input()
            if gameBoard.isValidColumn(column):
                gameBoard.addPiece(humanPiece, column)
                break
    else:
        humanPiece = 'b'
        aiPiece = 'r'
    blockPrint()
    computerAction = maxAI(gameBoard, aiPiece)
    gameBoard.addPiece(aiPiece, computerAction)
    enablePrint()
    while gameBoard.winner is None and not gameBoard.isFull():
        gameBoard.print()
        print("Select a number associated with the column you want to choose")
        while True:
            column = input()
            if gameBoard.isValidColumn(column):
                if gameBoard.addPiece(humanPiece, column)[0]:
                    print("You win!")
                break
        if gameBoard.winner is not None or gameBoard.isFull():
            break
        blockPrint()
        computerAction = maxAI(gameBoard, aiPiece)
        gameBoard.addPiece(aiPiece, computerAction)
        enablePrint()
    gameBoard.print()


if __name__ == "__main__":
    main()
