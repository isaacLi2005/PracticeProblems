def main():
    t = int(input())
    for i in range(t):
        inputVal = input().split(" ")
        inputVal = [int(v) for v in inputVal]
        [y, x] = inputVal

        squareGroup = max(y, x)
        base = (squareGroup ** 2) - (squareGroup - 1)
        if squareGroup % 2 == 0:
            adjustment = y - x
        else:
            adjustment = x - y
        print(base + adjustment)




main()