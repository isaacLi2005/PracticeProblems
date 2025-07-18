#include <iostream>
#include <algorithm>
#include <set>
#include <vector>

int main() {
    size_t n;
    std::cin >> n;
    std::vector<size_t> blocks(n);
    std::multiset<size_t> towerTops {};

    for (size_t i = 0; i < n; i++) {
        std::cin >> blocks[i];
    }

    for (size_t i = 0; i < n; i++) {
        auto largestBlockTopIt = towerTops.upper_bound(blocks[i]);
        if (largestBlockTopIt != towerTops.end()) {
            towerTops.erase(largestBlockTopIt);
        }
        towerTops.insert(blocks[i]);
    }

    std::cout << towerTops.size() << std::endl;

    return 0;
}