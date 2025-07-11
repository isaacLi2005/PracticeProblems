#include <algorithm>
#include <iostream>
#include <tuple>
 
int main() {
  int n{};
  int x{};
  std::cin >> n >> x;
 
  std::tuple<int, int> *values = new std::tuple<int, int>[n];
  int value{};
  for (int i = 0; i < n; i++) {
    std::cin >> value;
    values[i] = {value, i};
  }
 
  std::sort(values, values + n);
 
  int lowPointer{0};
  int highPointer{n - 1};
  int sum{};
  while (lowPointer < highPointer) {
    auto [lowValue, lowOriginalIndex] = values[lowPointer];
    auto [highValue, highOriginalIndex] = values[highPointer];
    sum = lowValue + highValue;
    if (sum == x) {
      std::cout << lowOriginalIndex + 1 << " " << highOriginalIndex + 1 << std::endl;
      return 0;
    } else if (sum < x) {
      lowPointer++;
    } else {
      highPointer--;
    }
  }
  std::cout << "IMPOSSIBLE" << std::endl;
 
  return 0;
}