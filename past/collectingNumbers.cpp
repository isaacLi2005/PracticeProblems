#include <iostream>
#include <vector>
#include <set>
 
int main() {
  size_t n {};
  std::cin >> n;
 
  std::vector<int> numbers(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> numbers[i];
  }
 
  int result {1};
  std::set<int> expectedNexts {1};
  for (size_t i = 0; i < n; i++) {
      if (expectedNexts.find(numbers[i]) == expectedNexts.end()) {
        expectedNexts.erase(numbers[i]);
        result++;
      }
      expectedNexts.insert(numbers[i]+1);
    }
 
  std::cout << result << std::endl;
 
  return 0;
}