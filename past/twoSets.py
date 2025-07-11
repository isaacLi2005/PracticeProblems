"""
Explanation:
 
By the known sum formula for arithmetic series, the sum s of the numbers 1, 2, ..., n is 
s = (n * (n + 1)) / 2. 
 
We notice that we can only create two groups that sum together to n if s is even; i.e.
s = (n * (n + 1)) / 2 = 2a for some integer a.
 
So then, solving for a,
a = (n / 4) * (n + 1) 
 
The method revolves around building "pairs" that sum up to n + 1. This is done by first
picking the pair (1, n), then (2, n-1), then (3, n-2), etc.
 
We can definitely use (n + 1) at least n // 4 times for a sum, where // is integer division. 
Also, if n is a multiple of 4, this works perfectly. 
 
Four cases: n % 4 = 0, 1, 2, 3. 
 
If 0, we are done. Use n + 1 a total of n//4 times and this groups perfectly. 
 
If 1, 
n = 4x + 1 for some x. 
s = (4x + 1)(4x + 2) / 2 = (4x + 1)(2x + 1) = 8x^2 + 6x + 1 which must be odd so we return NO in this case. 
 
If 2, 
n = 4x + 2 for some x. 
s = (4x + 2)(4x + 3) / 2 = (2x + 1)(4x + 3) = 8x^2 + 10x + 3 which must be odd so we return NO in this case. 
 
If 3, 
n = 4x + 3 for some x. 
(4x + 3)(4x + 4) / 2 = (4x + 3)(2x + 2) = 8x^2 + 12x + 6 which is even 
 
Now, I want to show an easy way to generate the two lists. After going through some examples, I notice that 
we can use x pairs of (n + 1) and then 3x + 3 in one list to make the half sum. A bunch of arithmetic manipulations
provides a basis for this. 
 
s = (n + 1)(n) / 2 = 2a
 
a = (n / 4)(n + 1)
a = ((4x + 3) / 4)(n + 1) = (x + 3/4)(n + 1) = x(n + 1) + 3/4(n + 1)
a = x(n + 1) + 3/4(4x + 4) = x(n + 1) + 3(x + 1)
 
We pick x pairs of (1, n), (2, n-1), (3, n-2)... then we have n - x + 1
as the largest number picked. Then n - x is the largest number remaining. 
And n - x = 4x + 3 - x = 3x + 3 = 3(x + 1), as desired. 
 
 
"""
 
def main():
  n = int(input())
 
  totalSum = (n * (n + 1)) // 2
 
  if totalSum % 2 == 1:
    print("NO")
    return
  
  firstList = []
 
  x = n // 4
  for i in range(x):
    firstList.append(i + 1)
    firstList.append(n - i)
  secondList = [i for i in range(x+1, n - x)]
 
  if n % 4 == 3:
    firstList.append(3 * x + 3)
  else:
    secondList.append(n - x)
 
 
  print("YES")
  print(len(firstList))
  print(*firstList)
  print(len(secondList))
  print(*secondList)
 
  
 
 
 
 
 
main()
