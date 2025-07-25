#include <iostream>
#include <unordered_map>
#include <cmath>

using namespace std;

const long long MOD = 1'000'000'007LL;

int main() {
    size_t n;
    cin >> n;

    size_t* values = new size_t[n];
    for (size_t i = 0; i < n; i++) {
        cin >> values[i];
    }

    unordered_map<size_t, size_t> valueAppearances;
    for (size_t i = 0; i < n; i++) {
        if (valueAppearances.find(values[i]) == valueAppearances.end()) {
            valueAppearances[values[i]] = 1;
        } else {
            valueAppearances[values[i]] += 1;
        }
    }

    size_t result = 1;
    for (auto& [key, value] : valueAppearances) {
        result = (result * (value + 1)) % MOD;
    }
    result -=1;

    delete[] values;
    cout << result << endl;
}