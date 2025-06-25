"""
Idea: The number of trailing zeroes is the number of times that 10 divides the number. 
We may find the number of times 10 dividides by the number of times that 5 divides the number, as
there are way more 2 factors. 
"""
 
import math
 
def main():
  n = int(input())
  result = 0
 
  power = 1
  
  addition = math.floor(n / (5 ** power))
  while addition > 0:
    result += addition
    power += 1
    addition = math.floor(n / 5 ** power)
 
  print(result)
 
main()