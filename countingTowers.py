import math

combMemo = dict()
def comb(n):
    """
    How many ways are there to use the numbers 1, 2, ..., n to 
    add up to n, with replacement and when order matters? 
    """
    if n in combMemo:
        return combMemo[n]
    else:
        result = 2 ** (n-1)
        combMemo[n] = result
        return result


countingMemo = dict()
def countingTowers(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 2
    elif n in countingMemo:
        return countingMemo[n]
    
    result = 0
    result += comb(n) ** 2 
    for i in range(1, n+1):
        result += (comb(i) * countingTowers(n-i))
    countingMemo[n] = result
    return result
    
    

print(countingTowers(3))