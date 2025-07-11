








def main():
    n = int(input())
    line = input().split(" ")
    line = [int(v) for v in line]

    expectedSum = n * (n + 1) // 2
    totalSum = sum(line)

    print(expectedSum - totalSum)


main()