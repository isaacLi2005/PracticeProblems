a, b = map(int, input().split(" "),)

memo = [[-1 for _ in range(b+1)] for _ in range(a+1)]

for i in range(min(a, b)+1):
    memo[i][i] = 0

"""
def helper(rows, cols):
    if rows == cols:
        return 0
    elif memo[rows][cols] != -1:
        return memo[rows][cols]
    
    candidateResults = []
    for rowSplit in range(1, (rows // 2)+1):
        lowerHeight = rows - rowSplit
        candidateResults.append(memo[rowSplit][cols] + memo[lowerHeight][cols])
    
    for colSplit in range(1, (cols // 2)+1):
        leftWidth = cols - colSplit
        candidateResults.append(memo[rows][colSplit] + memo[rows][leftWidth])
    
    result = min(candidateResults) + 1

    memo[rows][cols] = result
    if cols <= a and rows <= b:
        memo[cols][rows] = result
    return result
"""

def noneMin(a, b):
    if a == None:
        return b
    else:
        return(min(a,b))

for rows in range(1, a+1):
    for cols in range(1, b+1):
        if rows == cols:
            continue

        result = rows * cols * 2 + 1
        for rowSplit in range(1, (rows // 2)+1):
            lowerHeight = rows - rowSplit
            result = noneMin(result, memo[rowSplit][cols] + memo[lowerHeight][cols])
        
        for colSplit in range(1, (cols // 2)+1):
            leftWidth = cols - colSplit
            result = noneMin(result, memo[rows][colSplit] + memo[rows][leftWidth])

        result += 1
        memo[rows][cols] = result


print(memo[a][b])