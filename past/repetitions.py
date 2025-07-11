def main():
    s = input()

    if s == "":
        print(0)
        return

    longest = 1
    i = 1
    prevLetter = s[0]

    currCount = 1
    
    while i < len(s):
        if s[i] != prevLetter:
            currCount = 1
        else:
            currCount += 1
            if currCount >= longest:
                longest = currCount
        prevLetter = s[i]
        i += 1
    
    print(longest)


main()