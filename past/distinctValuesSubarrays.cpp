#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


int main() {
    size_t n;
    cin >> n;

    vector<size_t> contents(n);

    for (size_t i = 0; i < n; i++) {
        std::cin >> contents[i];
    }

    unordered_map<size_t, size_t> last;
    size_t left = 0;

    size_t count = 0;
    for (size_t right = 0; right < n; right++) {
        if (auto it = last.find(contents[right]); it != last.end() && it->second >= left)
            left = it->second + 1;

        count += right - left + 1;

        last[contents[right]] = right;
    }

    cout << count << endl;

    return 0;
}