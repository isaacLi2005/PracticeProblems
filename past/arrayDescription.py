# TODO: Switch the order of the array for locality. 


MOD = 10**9 + 7
def main():
    [n, m] = map(int, input().split())

    arrayValues = list(map(int, input().split()))

    # n is an index, m is a value
    memo = [[0] * n for _ in range(m+1)]

    # Special case where the first number is a 0
    if arrayValues[0] == 0:
        for i in range(1, m+1):
            memo[i][0] = 1
    else:
        memo[arrayValues[0]][0] = 1
    
    for j in range(n-1):
        if arrayValues[j] == 0:
            for i in range(1, m+1):
                if memo[i][j] == 0:
                    continue

                for shift in (-1, 0, 1):
                    if 1 <= i + shift <= m and (arrayValues[j+1] == 0 or arrayValues[j+1] == i + shift):
                        memo[i + shift][j+1] = (memo[i][j] + memo[i + shift][j+1]) % MOD
        else:
            for shift in (-1, 0, 1):
                if 1 <= arrayValues[j] + shift <= m and (arrayValues[j+1] == 0 or arrayValues[j+1] == arrayValues[j] + shift):
                    memo[arrayValues[j] + shift][j + 1] = (memo[arrayValues[j]][j] + memo[arrayValues[j] + shift][j + 1]) % MOD
    
    if arrayValues[n-1] == 0:
        result = 0
        for i in range(1, m+1):
            result = (result + memo[i][n-1]) % MOD
        print(result)
    else:
        print(memo[arrayValues[n-1]][n-1] % MOD)


main()