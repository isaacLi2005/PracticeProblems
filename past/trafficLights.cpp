#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <cassert>

int main() {
    int x;
    int n;
    std::cin >> x >> n;

    int* inputs = new int[n];
    for (int i {0}; i < n; i++) {
        std::cin >> inputs[i];
    }
    int* results = new int[n];

    std::set<int> trafficLightsIndicesSet {0, x};
    std::multiset<int> lengthsMultiset {x};
    for (int i {0}; i < n; i++) {
        int nextLightIndex {*trafficLightsIndicesSet.upper_bound(inputs[i])};

        auto prevLightIndexIt {trafficLightsIndicesSet.lower_bound(inputs[i])};
        assert(prevLightIndexIt != trafficLightsIndicesSet.begin());
        prevLightIndexIt--;
        int prevLightIndex  {*prevLightIndexIt};

        int brokenLength {nextLightIndex - prevLightIndex};

        lengthsMultiset.erase(lengthsMultiset.find(brokenLength));
        trafficLightsIndicesSet.insert(inputs[i]);
        lengthsMultiset.insert(inputs[i] - prevLightIndex);
        lengthsMultiset.insert(nextLightIndex - inputs[i]);

        results[i] = *lengthsMultiset.rbegin();
    }

    for (int i = 0; i < n; i++) {
        std::cout << results[i] << " ";
    }
    std::cout << std::endl;

    

    delete[] inputs;
    delete[] results;


    return 0;
}