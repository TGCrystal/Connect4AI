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

    def addPiece(self, piece, column):
        if self.board[self.rows - 1][column] != '0':
            return "Error"
        i = self.rows - 1
        while i >= 0 and self.board[i][column] == '0':
            i -= 1
        self.board[i+1][column] = piece

    def print(self):
        i = self.rows - 1
        while i >= 0:
            print(self.board[i])
            i -= 1
        print(['#', '#', '#', '#', '#', '#', '#'])
        print(['1', '2', '3', '4', '5', '6', '7'])
