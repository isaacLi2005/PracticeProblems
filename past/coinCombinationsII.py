MOD = (10 ** 9) + 7

def coinCombinations(x, coinsList):
    memo = [0] * (x + 1)
    memo[0] = 1

    for coin in coinsList:
        for target in range(1, x + 1):
            priorSum = target - coin
            if priorSum >= 0:
                priorWays = memo[priorSum]
                memo[target] = (memo[target] + priorWays) % MOD
    
    print(memo[x])

def main():
    (n, x) = list(map(int, input().split()))
    coinsList = list(map(int, input().split()))

    coinCombinations(x, coinsList)

main()