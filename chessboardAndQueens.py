def isValidPlacement(coords, queensL, reservedSquares):
    (newRow, newCol) = coords
    if (newRow, newCol) in reservedSquares:
        return False
    for (oldRow, oldCol) in queensL:
        if (newRow == oldRow 
            or newCol == oldCol 
            or abs(newRow - oldRow) == abs(newCol - oldCol)):
            return False
    return True
 
def chessboardAndQueensH(row, reservedSquares, currQueens):
    if row == 8:
        return 1  
 
    result = 0
    for col in range(8):
        if isValidPlacement((row, col), currQueens, reservedSquares):
            currQueens.append((row, col))
            result += chessboardAndQueensH(row + 1, reservedSquares, currQueens)
            currQueens.pop()
    return result
 
def main():
    reservedSquares = set()
    for i in range(8):
        row = input()
        for j in range(8):
            if row[j] == "*":
                reservedSquares.add((i, j))
 
    print(chessboardAndQueensH(0, reservedSquares, []))
 
main()