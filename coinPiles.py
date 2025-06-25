def coinPilesH(a, b):
  difference = abs(a - b)
  confluence = min(a, b) - difference
  if confluence >= 0 and confluence % 3 == 0 :
    print("YES")
  else:
    print("NO")
 
 
def main():
  t = int(input())
  for _ in range(t):
    a, b = map(int, input().split(" "))
    coinPilesH(a, b)
 
main()