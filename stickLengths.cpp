#include <algorithm>
#include <iostream>
 
int main() {
  int n{};
  std::cin >> n;
 
  long long *lengths = new long long[n];
  for (size_t i{0}; i < n; i++) {
    std::cin >> lengths[i];
  }
  std::sort(lengths, lengths + n);
 
  long long median{lengths[n / 2]};
 
  long long result{0};
  for (size_t i{0}; i < n; i++) {
    result += abs(median - lengths[i]);
  }
 
  std::cout << result << std::endl;
 
  return 0;
}