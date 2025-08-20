from typing import List

def retrieveMemoValue(memo: List[List[int]], m: int, n: int, i: int, j: int):
    if not (0 <= i < m and 0 <= j < n):
        return 0
    
    return memo[i][j]

def recoverLongest(memo: List[List[int]], A: List[int], B: List[int]):
    m, n = len(memo), len(memo[0])

    result = []

    i, j = m-1, n-1




    while i >= 0 and j >= 0:
        diag = retrieveMemoValue(memo, m, n, i-1, j-1)  # CHANGED
        up = retrieveMemoValue(memo, m, n, i-1, j)    # CHANGED
        left = retrieveMemoValue(memo, m, n, i, j-1)    # CHANGED
        if A[i] == B[j] and memo[i][j] == diag + 1:
            result.append(A[i])
            i -= 1 
            j -= 1
        elif up == memo[i][j] and up >= left:
            i -= 1  
        else:
            j -= 1

    result.reverse()
    return result


def longestSubsequence(A: List[int], B: List[int]):
    m = len(A)
    n = len(B)

    memo = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if A[i] != B[j]:
                memo[i][j] = max(
                    retrieveMemoValue(memo, m, n, i-1, j),
                    retrieveMemoValue(memo, m, n, i, j-1)
                )
            else:
                memo[i][j] = max(
                    retrieveMemoValue(memo, m, n, i-1, j),
                    retrieveMemoValue(memo, m, n, i-1, j-1) + 1,
                    retrieveMemoValue(memo, m, n, i, j-1)
                )
    
    lengthOfLongest = memo[m-1][n-1]
    example = recoverLongest(memo, A, B)

    return (lengthOfLongest, example)




def main():
    firstLine = input()
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    
    (lengthOfLongest, example) = longestSubsequence(A, B)
    print(lengthOfLongest)
    for val in example:
        print(val)

main()