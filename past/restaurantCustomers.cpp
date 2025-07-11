#include <algorithm>
#include <iostream>
#include <vector>
 
int main() {
  int n{};
  std::cin >> n;
  std::vector<std::tuple<int, int>> customers(2 * n);
 
  int enter{};
  int leave{};
  for (int i = 0; i < n; i++) {
    std::cin >> enter >> leave;
    customers[2 * i] = {enter, 1};
    customers[2 * i + 1] = {leave, -1};
  }
 
  std::sort(customers.begin(), customers.end());
 
  int largest{0};
  int current{0};
 
  for (int j = 0; j < 2 * n; j++) {
    auto [firstElem, secondElem] = customers[j];
    current = current + secondElem;
    largest = std::max(largest, current);
  }
 
  std::cout << largest << std::endl;
 
  return 0;
}