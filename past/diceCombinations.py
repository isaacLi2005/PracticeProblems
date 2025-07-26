CON = (10 ** 9) + 7

import sys

n = int(input())
memo = [0] * (n + 1)
memo[0] = 1
def helper(k):
    if k < 0:
        return 0
    elif 0 <= k <= 1:
        return 1
    elif memo[k] != 0:
        return memo[k]
    
    result = 0
    for lastVal in range(1, 7):
        result = (result + helper(k-lastVal)) % CON
    memo[k] = result
    return result

for i in range(1, n+1):
    memo[i] = helper(i)

print(helper(n))