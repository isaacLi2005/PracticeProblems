import typing

def numPossible(n: int):
    if n <= 1:
        print(0)
        return

    totalPossible = ((n ** 2) * (n ** 2 - 1)) // 2

    rectanglesPossible = ((n - 1) * (n - 2)) * 2
    attackPositionsPossible = rectanglesPossible * 2

    print(totalPossible - attackPositionsPossible)


def main():
    n = int(input())

    for i in range(1, n + 1):
        numPossible(i)

main()