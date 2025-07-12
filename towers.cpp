#include <iostream>
#include <algorithm>
#include <multiset>
#include <array>

int main() {
    size_t n;
    std::cin >> n;
    std::array<size_t> blocks(n);
    std::multiset<size_t> towerTops {};

    for (size_t i = 0; i < n; i++) {
        std::cin >> blocks[i];
    }

    for (size_t i = 0; i < n; i++) {
        auto largestBlockTopIt = towerTops.upper_bound(blocks[i]);
        if (largestBlockTopIt == towerTops.end()) {
            towerTops.add
        }
    }



    return 0
}