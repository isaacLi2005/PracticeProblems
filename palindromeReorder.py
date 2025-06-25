def main():
  inputString = input()
 
  letterCounter = dict()
  for char in inputString:
    if char not in letterCounter:
      letterCounter[char] = 1
    else:
      letterCounter[char] += 1
  
  currentOddChar = ""
  for key in letterCounter:
    if letterCounter[key] % 2 == 1:
      if currentOddChar != "":
        print("NO SOLUTION")
        return
      else:
        currentOddChar = key
 
 
  result = ""
  for letter in letterCounter:
    count = letterCounter[letter] // 2
    result += letter * count
 
  
 
  result = result[::-1] + currentOddChar + result
  
  print(result)
  return
  
 
main()