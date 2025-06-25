def grayCodeH(n):
  if n == 0:
    return []
  elif n == 1:
    return ["0", "1"]
  else:
    previous = grayCodeH(n-1)
    firstHalf = [v + "0" for v in previous]
    secondHalf = [v + "1" for v in previous[::-1]]
    return firstHalf + secondHalf
 
def main():
  n = int(input())
 
  for v in grayCodeH(n):
    print(v)
 
main()