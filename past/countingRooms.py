from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(startRow, startCol, grid, visited):
    rows, cols = len(grid), len(grid[0])


    queue = deque([(startRow, startCol)])
    visited[startRow][startCol] = True
    while len(queue) > 0:
        (row, col) = queue.popleft()

        for rowChange, colChange in DIRECTIONS:
            newRow, newCol = row + rowChange, col + colChange

            if (0 <= newRow < rows and 0 <= newCol < cols 
                and not visited[newRow][newCol]
                and grid[newRow][newCol] == "."):
                queue.append((newRow, newCol))
                visited[newRow][newCol] = True


def countingRooms(n, m, grid):
    visited = [[False for _ in range(m)] for _ in range(n)]

    rooms = 0
    for row in range(n):
        for col in range(m):
            if grid[row][col] == "." and not visited[row][col]:
                rooms += 1
                bfs(row, col, grid, visited)
    return rooms
        


def main():
    [n, m] = map(int, input().split(" "))

    grid = []
    for _ in range(n):
        grid.append(input())

    numRooms = countingRooms(n, m, grid)
    print(numRooms)

main()