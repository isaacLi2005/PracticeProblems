def creatingStringsH(charDict):
  if charDict == dict():
    return [""]
  else:
    result = []
    allKeys = charDict.keys()
    for char in set(allKeys):
      if charDict[char] == 1:
        charDict.pop(char)
      else:
        charDict[char] -= 1
        
      smallerResult = creatingStringsH(charDict)
      smallerResult = [char + v for v in smallerResult]
      result += smallerResult
 
      if char not in charDict:
        charDict[char] = 1
      else:
        charDict[char] += 1
    
    return result
 
def main():
  s = input()
 
  charDict = dict()
  for char in s:
    if char not in charDict:
      charDict[char] = 1
    else:
      charDict[char] += 1
 
  result = creatingStringsH(charDict)
  result.sort()
  
  print(len(result))
  for s in result:
    print(s)
 
 
 
main()