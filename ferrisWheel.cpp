#include <iostream>
#include <array>
#include <algorithm>

int main() {
    int n {};
    int k {};

    std::cin >> n >> k;

    int* children = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> children[i];
    }
    std::sort(children, children + n);


    int heaviestChildIndex {n-1};
    int lightestChildIndex {0};
    int count {0};
    int heaviestChildWeight {};
    int lightestChildWeight {};

    while (heaviestChildIndex >= lightestChildIndex) {
        if (heaviestChildIndex == lightestChildIndex) {
            count++;
            break;
        } else {
            heaviestChildWeight = children[heaviestChildIndex];
            lightestChildWeight = children[lightestChildIndex];
            if (lightestChildWeight + heaviestChildWeight <= k) {
                lightestChildIndex++;
            }
            
            heaviestChildIndex--;
            count++;
        }

    }


    delete[] children;

    std::cout << count << "\n";

    return 0;
}