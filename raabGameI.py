def raabGameWrapper(n, a, b):
    ties = n - (a + b)

    if a + b > n or a == n or b == n:
        print("NO")
        return
    
    B = [0] * n
    seen = set()
    
    # Fill Ties
    for cardValue in range(b+1, n-a+1):
        seen.add(cardValue)
        B[cardValue-1] = cardValue

    # Fill Player 2 Losses
    cardValue = n
    for i in range(b-1, -1, -1):
        while cardValue in seen:
            cardValue -= 1
        B[i] = cardValue
        seen.add(cardValue)

    # Fill Player 2 losses
    cardValue = 1
    for i in range(n-a, n):
        while cardValue in seen:
            cardValue += 1
        B[i] = cardValue
        seen.add(cardValue)

    A=list(range(1,n+1))
    for i in range(n):
        if A[i]>B[i]:
            a-=1
        elif B[i]>A[i]:
            b-=1

    if a!=b or a!=0:
        print("NO")
        return
    print("YES")
    print(" ".join(map(str,A)))
    print(" ".join(map(str,B)))
    
    print("YES")
    print(" ".join([str(i) for i in range(1, n + 1)]))
    print(" ".join([str(v) for v in B]))



def main():
    t = int(input())
    for _ in range(t):
        line = input()
        lineList = line.split(" ")
        n = int(lineList[0])
        a = int(lineList[1])
        b = int(lineList[2])
        raabGameWrapper(n, a, b)

main()