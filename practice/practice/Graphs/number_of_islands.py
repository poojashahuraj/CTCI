# Program to count islands in boolean 2D matrix
class Graph:
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g

    # A function to check if a given cell (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number is in range and
        # value is 1 and not yet visited
        return (0 <= i < self.ROW and
                0 <= j < self.COL and
                not visited[i][j] and
                self.graph[i][j] == 1)

    # A utility function to do DFS for a 2D 
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):

        # These arrays are used to get row and column numbers of 8 neighbours of a given cell
        row_num = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_num = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited
        visited[i][j] = True

        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + row_num[k], j + col_num[k], visited):
                self.DFS(i + row_num[k], j + col_num[k], visited)

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def countIslands(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Initialize count as 0 and traverse through the all cells of given matrix.
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, 
                # then new island found
                if not visited[i][j] and self.graph[i][j] == 1:
                    # Visit all cells in this island 
                    # and increment island count
                    self.DFS(i, j, visited)
                    count += 1

        return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print "Number of islands is :"
print g.countIslands()

# This code is contributed by Neelam Yadav
