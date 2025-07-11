def main():
    n = int(input())

    if n == 1:
        print(1)
        return
    elif n == 2 or n == 3:
        print("NO SOLUTION")
        return
    elif n == 4:
        print("3 1 4 2")
        return

    odds = []
    i = 1
    while i <= n:
        odds.append(i)
        i += 2
    
    evens = []
    j = 2
    while j <= n:
        evens.append(j)
        j += 2
    
    results = odds + evens
    for v in results:
        print(v, end = " ")
    print()

main()

