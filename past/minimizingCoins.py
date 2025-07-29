from typing import List, Dict, Set
import sys

def minimizing_coins(x: int, coins):
    INF = 10 ** 9       
    dp = [INF] * (x + 1) 
    dp[0] = 0        

    for s in range(0, x + 1):
        for coin in coins:
            cand = dp[s - coin] + 1
            if cand < dp[s]:
                dp[s] = cand

    print(dp[x] if dp[x] != INF else -1)


def main() -> None:
    n, x = map(int, sys.stdin.readline().split())
    coins = list(map(int, sys.stdin.readline().split()))
    minimizing_coins(x, coins)

if __name__ == "__main__":
    main()