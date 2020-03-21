class board:
    def __init__(self):
        self.columns = 7
        self.rows = 6
        self.board = []
        i = 0
        while i < self.rows:
            j = 0
            column = []
            while j < self.columns:
                column.append('0')
                j += 1
            self.board.append(column)
            i += 1

    def isFull(self):
        i = 0
        while i < self.rows:
            j = 0
            while j < self.columns:
                if self.board[i][j] == '0':
                    return False
                j += 1
            i += 1
        return True

    def gameWon(self, piece, row, column):
        # check vertical
        space = 1
        i = row - 1
        while i >= 0 and self.board[i][column] == piece:
            space += 1
            i -= 1
        i = row + 1
        while i < self.rows and self.board[i][column] == piece:
            space += 1
            i += 1
        if space >= 4:
            return True

        # check horizontal
        space = 1
        j = column - 1
        while j >= 0 and self.board[row][j] == piece:
            column += 1
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
        while i >= 0 and j < self.comumns and self.board[i][j] == piece:
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

    def addPiece(self, piece, column):
        if self.board[self.rows - 1][column] != '0':
            return "Error"
        i = self.rows - 1
        while i >= 0 and self.board[i][column] == '0':
            i -= 1
        i += 1
        self.board[i][column] = piece
        return self.gameWon(piece, i, column)

    def print(self):
        i = self.rows - 1
        while i >= 0:
            print(self.board[i])
            i -= 1
        print(['#', '#', '#', '#', '#', '#', '#'])
        print(['0', '1', '2', '3', '4', '5', '6'])
        print()
