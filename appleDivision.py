def main():
  n = int(input())
  L = input().split(" ")
  L = [int(v) for v in L]
  L.sort()
  
  totalSum = sum(L)
 
  def appleDivisionH(i, firstSum, secondSum):
    if i == len(L) - 1:
      element = L[i]
      return min(abs(firstSum + element - secondSum), abs(firstSum - secondSum - element))
    else:
      include = appleDivisionH(i+1, firstSum + L[i], secondSum)
      notInclude = appleDivisionH(i+1, firstSum, secondSum + L[i])
      return min(include, notInclude)
  
  print(appleDivisionH(0, 0, 0))
 
