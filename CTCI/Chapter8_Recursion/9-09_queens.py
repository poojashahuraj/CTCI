"""
Write an algorithm to print all ways of arranging eight queens on an 8x8
# chess board so that none of them share the same row, column or diagonal. In
# this case, "diagonal" means all diagonals, not just the two that bisect the
# board.
"""

class ChessBoard():
    def __init__(self, size):
        # this dict will store row number as key and column number as value
        self.queens = dict()
        self.size = size
        pass
    def check_available(self, row, column):
        for k, v in self.queens.items():
            if k == row:
                return False
            if v == column:
                return False

            # To check is two elements are diagonal we check if diff between column and row is same.
            if abs(row - k) == abs(column - v):
                return False
        return True

    def put_queens(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.check_available(i,j):
                    self.queens[i] = j
                    break
            if i not in self.queens.keys():
                print "{} was not placed".format(i)
        print self.queens

c = ChessBoard(8)
c.put_queens()
