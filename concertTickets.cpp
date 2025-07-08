#include <iostream>
#include <set>
#include <vector>

int main() {
    int n {};
    int m {};
    std::cin >> n >> m;

    std::multiset<int> priceSet;
    
    int ticketPrice {};
    for (int i = 0; i < n; i++) {    
        std::cin >> ticketPrice;
        priceSet.insert(ticketPrice);
    }

    int customerPrice {};
    std::multiset<int>::iterator largestAvailable {};
    for (int j = 0; j < m; j++) {
        std::cin >> customerPrice;
        largestAvailable = priceSet.upper_bound(customerPrice);
        if (largestAvailable == priceSet.begin()) {
            std::cout << -1 << "\n";
        } else {
            largestAvailable--;
            std::cout << *largestAvailable << "\n";
            priceSet.erase(largestAvailable);

        }

    }


    

    return 0;
}