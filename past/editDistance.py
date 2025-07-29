def editDistance(s1, s2):
  m = len(s1)
  n = len(s2)
  memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
 
  for i in range(m+1):
    memo[i][0] = i
  
  for j in range(n+1):
    memo[0][j] = j
 
  for firstCharacters1 in range(1, m+1):
    for firstCharacters2 in range(1, n+1):
      resultFromDeletion = memo[firstCharacters1 - 1][firstCharacters2] + 1
      resultFromInsertion = memo[firstCharacters1][firstCharacters2 - 1] + 1
      resultFromReplacement = memo[firstCharacters1-1][firstCharacters2-1] + (1 if s1[firstCharacters1-1] != s2[firstCharacters2-1] else 0)
 
      memo[firstCharacters1][firstCharacters2] = min(resultFromDeletion, resultFromInsertion, resultFromReplacement)
 
  print(memo[m][n])
 
def main():
  s1 = input()
  s2 = input()
 
  editDistance(s1, s2)
 
main()