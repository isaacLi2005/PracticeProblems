def towersH(n, source, temp, dest, currentMoves):
  if n == 0:
    return 0
  elif n == 1:
    currentMoves.append((source, dest))
    return 1
  else:
    firstSubMoves = towersH(n - 1, source, dest, temp, currentMoves)
    currentMoves.append((source, dest))
    secondSubMoves = towersH(n - 1, temp, source, dest, currentMoves)
    return firstSubMoves + 1 + secondSubMoves
  
 
def main():
  n = int(input())
 
  currentMoves = []
  numMoves = towersH(n, 1, 2, 3, currentMoves)
  print(numMoves)
  for (start, end) in currentMoves:
    print(start, end)
 
main()