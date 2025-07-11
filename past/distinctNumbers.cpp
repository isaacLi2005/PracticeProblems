#include <iostream>
#include <set>

int main() {

    int count {0};
    std::set<int> seen;

    int n; 
    std::cin >> n;

    int curr;
    for (int i = 0; i < n; i++) {
        std::cin >> curr;
        if (seen.count(curr) == 0) {
            count++;
            seen.insert(curr);
        }

    }


    std::cout << count << "\n";


    return 0;
}
