def findAvailable(restrictedChars):
    for char in ["A", "B", "C", "D"]:
        if char not in restrictedChars:
            return char
    raise ValueError
        
def isValidSquare(rows, cols, i, j):
    return 0 <= i < rows and 0 <= j < cols


def main():
    firstLine = list(map(int, input().split(" ")))
    rows = firstLine[0]
    cols = firstLine[1]

    grid = []

    for _ in range(rows):
        grid.append([c for c in input()])

    for i in range(rows):
        for j in range(cols):
            restrictedLetters = []
            restrictedLetters.append(grid[i][j])
            if isValidSquare(rows, cols, i - 1, j):
                restrictedLetters.append(grid[i-1][j])
            if isValidSquare(rows, cols, i, j-1):
                restrictedLetters.append(grid[i][j-1])
            newLetter = findAvailable(restrictedLetters)
            grid[i][j] = newLetter
    
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j], end= "")
        print()

    





main()