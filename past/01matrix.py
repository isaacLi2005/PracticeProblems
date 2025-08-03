class Solution:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def isValidIndex(self, rows, cols, row, col):
        return 0 <= row < rows and 0 <= col < cols

    def updateWithNum(self, result, mat, coordSet, num):
        m = len(result)
        n = len(result[0])

        newNeighbors = set()

        for (row, col) in coordSet:
            result[row][col] = num
            for (rowChange, colChange) in self.directions:
                (newRow, newCol) = (row + rowChange, col + colChange)
                if (
                    self.isValidIndex(m, n, newRow, newCol)
                    and result[newRow][newCol] == -1
                    and mat[newRow][newCol] == 1
                    and (newRow, newCol) not in coordSet
                ):
                    newNeighbors.add((newRow, newCol))
        return newNeighbors


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        result = [[-1 for _ in range(n)] for _ in range(m)]


        nextNeighbors = set()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    result[row][col] = 0
                    for (dr, dc) in self.directions:
                        nr, nc = row + dr, col + dc
                        if (
                            self.isValidIndex(m, n, nr, nc) 
                            and mat[nr][nc] == 1
                        ):
                            nextNeighbors.add((nr, nc))
        
        currNextDist = 1
        while len(nextNeighbors) > 0:
            nextNeighbors = self.updateWithNum(result, mat, nextNeighbors, currNextDist)
            currNextDist += 1

        
        return result