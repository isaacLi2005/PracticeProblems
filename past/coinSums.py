n = int(input())
coins = list(map(int, input().split()))

resultSet = set()

for coin in coins:
    newSums = set()
    for prevSum in resultSet:
        newSums.add(prevSum + coin)
    resultSet = resultSet.union(newSums)
    resultSet.add(coin)

print(len(resultSet))

for sum in sorted(list(resultSet)):
    print(sum, end = " ")
print()