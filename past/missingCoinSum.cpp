#include <algorithm>
#include <iostream>
 
int main() {
  long long n{};
  std::cin >> n;
 
  long long *coins = new long long[n];
  for (size_t i = 0; i < n; i++) {
    std::cin >> coins[i];
  }
  std::sort(coins, coins + n);
 
  long long smallestUnreachable{1};
  for (size_t i = 0; i < n; i++) {
    if (smallestUnreachable < coins[i]) {
      std::cout << smallestUnreachable << std::endl;
      return 0;
    } else {
      smallestUnreachable += coins[i];
    }
  }
 
  long long fallBack{0};
  for (size_t i = 0; i < n; i++) {
    fallBack += coins[i];
  }
  std::cout << fallBack + 1 << std::endl;
 
  delete[] coins;
 
  return 0;
}