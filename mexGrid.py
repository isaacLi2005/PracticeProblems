def main():
    n = int(input())

    result = [[0] * n for i in range(n)]

    for r in range(n):
        for c in range(n):
            result[r][c] = r ^ c

    for r in range(n):
        for c in range(n):
            print(result[r][c], end = " ")
        print()

main()