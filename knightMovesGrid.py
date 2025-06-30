from collections import deque

class Queue:
    def __init__(self):
        self._dq = deque()              

    def dequeue(self):
        if not self._dq:
            raise IndexError("pop from empty queue")
        return self._dq.popleft()       

    def enqueue(self, val):
        self._dq.append(val)           

    def isEmpty(self):
        return not self._dq            


def isValidSquare(n, r, c, restrictGrid = False):
    if restrictGrid:
        return 0 <= r < n and 0 <= c < n and r <= 3 and c <= 3
    else:
        return 0 <= r < n and 0 <= c < n
    
def hardcoded_4x4_base_grid():
    # Minimum knight moves from (0,0) to each position in 4x4 grid
    return [
        [0, 3, 2, 3],
        [3, 4, 1, 2],
        [2, 1, 4, 3],
        [3, 2, 3, 2]
    ]

def hardcoded_4x4_only_grid():
    # Minimum knight moves from (0,0) to each position in 4x4 grid
    return [
        [0, 3, 2, 5],
        [3, 4, 1, 2],
        [2, 1, 4, 3],
        [5, 2, 3, 2]
    ]


def main():
    n = int(input())

    if n == 4:
        grid = hardcoded_4x4_only_grid()
        for row in range(n):
            for col in range(n):
                print(grid[row][col], end=" ")
            print()
        return



    grid = [[None] * n for _ in range(n)]

    base = hardcoded_4x4_base_grid()
    for r in range(4):
        for c in range(4):
            grid[r][c] = base[r][c]

    """
    grid[0][0] = 0


    queue = Queue()

    queue.enqueue((0, 0, 0))

    knightHorizontalMoves = [(2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (1, 2)]

    while not queue.isEmpty():
        (row, col, val) = queue.dequeue()

        for (rowMove, colMove) in knightHorizontalMoves:
            (newRow, newCol) = (row + rowMove, col + colMove)
            if isValidSquare(n, newRow, newCol, True) and (grid[newRow][newCol] == None or grid[newRow][newCol] > val + 1):
                grid[newRow][newCol] = val + 1
                queue.enqueue((newRow, newCol, val + 1))
    """





    knightRowRingMoves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    knightColRingMoves = [(-2, -1), (-1, -2), (1, -2), (-1, 2)]


    for ring in range(4, n):
        # The horizontal
        for ringCol in range(ring + 1):
            min = None
            for (rowMove, colMove) in knightRowRingMoves:
                if isValidSquare(n, ring + rowMove, ringCol + colMove):
                    gridValue = grid[ring + rowMove][ringCol + colMove]
                    if gridValue is not None and (min is None or gridValue + 1 < min):
                        min = gridValue + 1
            grid[ring][ringCol] = min

        # The vertical
        for ringRow in range(ring):
            min = None
            for (rowMove, colMove) in knightColRingMoves:
                if isValidSquare(n, ringRow + rowMove, ring + colMove):
                    gridValue = grid[ringRow + rowMove][ring + colMove]
                    if gridValue is not None and (min is None or gridValue + 1 < min):
                        min = gridValue + 1
            grid[ringRow][ring] = min


    for row in range(n):
        for col in range(n):
            print(grid[row][col], end=" ")
        print()





main()