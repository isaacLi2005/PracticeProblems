import sys
sys.setrecursionlimit(1000005)


import math

n = int(input())

def numDigits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(n)) + 1

def extractDigit(n, i):
    if n == 0:
        return 0
    digits = numDigits(n)
    return (n // (10 ** (digits - i - 1))) % 10

memo = [None] * (n + 1)
memo[0] = 0
for i in range(1, n + 1):
    best = None
    usedSet = set()
    t = i
    while t > 0:
        digit = t % 10
        if digit == 0 or digit in usedSet:
            t //= 10
            continue
        smallerResult = memo[i - digit]
        if best is None or smallerResult < best:
            best = smallerResult
        t //= 10
    memo[i] = 1 + best


print(memo[n])
