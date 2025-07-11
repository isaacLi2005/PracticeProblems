#include <algorithm>
#include <iostream>
#include <vector>
 
bool endtimeSorter(std::tuple<int, int> &a, std::tuple<int, int> &b) {
  auto [a1, a2] = a;
  auto [b1, b2] = b;
 
  if (a2 != b2) {
    return a2 < b2;
  } else {
    return a1 < b1;
  }
}
 
int main() {
  int n{};
  std::cin >> n;
 
  std::vector<std::tuple<int, int>> movieTimes(n);
  int start, end;
  for (int i = 0; i < n; i++) {
    std::cin >> start >> end;
    movieTimes[i] = {start, end};
  }
 
  std::sort(movieTimes.begin(), movieTimes.end(), endtimeSorter);
 
  int count{0};
  int lastEndtime{0};
  for (int i = 0; i < n; i++) {
    auto [start, end] = movieTimes[i];
    if (start >= lastEndtime) {
      lastEndtime = end;
      count++;
    }
  }
 
  std::cout << count << std::endl;
 
  return 0;
}