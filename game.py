class board:
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.board = []
        self.winner = None
        i = 0
        while i < self.rows:
            j = 0
            column = []
            while j < self.columns:
                column.append('0')
                j += 1
            self.board.append(column)
            i += 1

    # Returns True if j is a column that a piece can be placed in, False otherwise w/ reason printed
    def isValidColumn(self, j):
        if not (isinstance(j, int) or j.isdigit()):
            print("Input is not an integer or convertible to an integer")
            return False
        j = int(j)
        if j < 0 or j >= self.columns:
            print("Please enter a number between 0 and ", self.columns)
            return False
        if self.board[self.rows-1][j] != '0':
            print("This column is already full")
            return False
        return True

    # Returns a list of valid columns
    def getValidMoves(self):
        moves = []
        i = 0
        while i < self.columns:
            if self.isValidColumn(i):
                moves.append(i)
            i += 1
        return moves

    # Returns True if the board is full, False otherwise, assumes pieces are added correctly
    def isFull(self):
        j = 0
        while j < self.columns:
            if self.board[self.rows - 1][j] == '0':
                return False
            j += 1
        return True

    # Returns true if adding a piece to specified row and column of the board results in a win, false otherwise
    def gameWon(self, piece, row, column):
        # check vertical
        space = 1
        i = row - 1
        while i >= 0 and self.board[i][column] == piece:
            space += 1
            i -= 1
        if space == 4:
            return True

        # check horizontal
        space = 1
        j = column - 1
        while j >= 0 and self.board[row][j] == piece:
            space += 1
            j -= 1
        j = column + 1
        while j < self.columns and self.board[row][j] == piece:
            space += 1
            j += 1
        if space >= 4:
            return True

        # check one diagonal
        space = 1
        i = row - 1
        j = column - 1
        while i >= 0 and j >= 0 and self.board[i][j] == piece:
            space += 1
            i -= 1
            j -= 1
        i = row + 1
        j = column + 1
        while i < self.rows and j < self.columns and self.board[i][j] == piece:
            space += 1
            i += 1
            j += 1
        if space >= 4:
            return True

        # check other diagonal
        space = 1
        i = row - 1
        j = column + 1
        while i >= 0 and j < self.columns and self.board[i][j] == piece:
            space += 1
            i -= 1
            j += 1
        i = row + 1
        j = column - 1
        while i < self.rows and j >= 0 and self.board[i][j] == piece:
            space += 1
            i += 1
            j -= 1
        if space >= 4:
            return True

        return False

    # Call isValidColumn before attempting to place
    # Adds piece to top of given column, column index starts at 0
    def addPiece(self, piece, column):
        column = int(column)
        i = self.rows - 1
        while i >= 0 and self.board[i][column] == '0':
            i -= 1
        i += 1
        self.board[i][column] = piece
        if self.gameWon(piece, i, column):
            self.winner = piece
            return True, i
        return False, i

    # Removes piece from given location
    def resetPosition(self, row, column):
        self.board[row][column] = '0'
        self.winner = None

    # Prints the current board layout with column labels below
    def print(self):
        i = self.rows - 1
        while i >= 0:
            print(self.board[i])
            i -= 1
        print(['#', '#', '#', '#', '#', '#', '#'])
        print(['0', '1', '2', '3', '4', '5', '6'])
        print()
