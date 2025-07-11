import math

def findDigitRanges(i, memo):
    if i == 1:
        return (1, 9)
    elif i in memo:
        return memo[i]
    else:
        (pastStart, pastEnd) = findDigitRanges(i-1, memo)

        firstValue = 10 ** (i - 1)
        lastValue = (10 ** i) - 1
        amountOfNumbers = lastValue - firstValue + 1

        newEnd = pastEnd + (i * amountOfNumbers) 
        result = (pastEnd + 1, newEnd)
        memo[i] = result
        return result
    

def numDigits(n):
    return len(str(n))


def getDigit(n, i):
    digitCount = numDigits(n)
    n //= 10 ** (digitCount - i - 1)
    return n % 10

def digitQueriesH(k, memo):
    if 1 <= k <= 9:
        print(k)
        return

    numDigits = 1
    (rangeStart, rangeEnd) = findDigitRanges(1, memo)
    while not rangeStart <= k <= rangeEnd:
        numDigits += 1
        (rangeStart, rangeEnd) = findDigitRanges(numDigits, memo)

    relativeIndex = k - rangeStart
    relevantNumber = relativeIndex // numDigits
    relevantIndexOfNumber = relativeIndex % numDigits

    number = (10 ** (numDigits - 1)) + relevantNumber
    relevantDigit = getDigit(number, relevantIndexOfNumber)

    print(relevantDigit)
    return


def main():
    q = int(input())
    memo = dict()
    for _ in range(q):
        digitQueriesH(int(input()), memo)

main()
