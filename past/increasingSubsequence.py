from typing import List
import bisect

def increasingSubsequence(L: List[int]):
    n = len(L)

    memo = [float("inf") for _ in range(n+1)]
    highestLength = 0

    for val in L:
        targetIndex = bisect.bisect_left(memo, val)
        memo[targetIndex] = val

        highestLength = max(highestLength, targetIndex + 1)
    
    return highestLength





def main():
    n = int(input())
    L = list(map(int, input().split(" ")))

    result = increasingSubsequence(L)

    print(result)

main()