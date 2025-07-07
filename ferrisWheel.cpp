#include <iostream>
#include <array>

int main() {
    int n {};
    int k {};

    const int constN {n};

    std::cin >> n >> k;

    std::array<int, constN> children = {};

    for (int i = 0; i < n; i++) {
        std::cin >> children[i];
    }

    int count {0};
    int heaviestChildIndex {n-1};

    int heaviestWeight {};
    int weightRemaining {};

    int secondHeaviestIndex {};
    int secondHeaviestWeight {};

    while (heaviestChildIndex >= 0) {
        if (children[heaviestChildIndex] == -1) {
            heaviestChildIndex--;
            continue;
        }
        heaviestWeight = children[heaviestChildIndex];
        children[heaviestChildIndex] = -1;
        weightRemaining = k - heaviestWeight;

        secondHeaviestIndex = heaviestChildIndex - 1;
        while (secondHeaviestIndex >= 0) {
            secondHeaviestWeight = children[secondHeaviestIndex];
            if (secondHeaviestWeight == -1) {
                secondHeaviestIndex--;
                continue;
            } else if (secondHeaviestWeight <= weightRemaining) {
                children[secondHeaviestWeight] = -1;
                break;
            }
        }
        count++;
    }

    std::cout << count;

    return 0;
}