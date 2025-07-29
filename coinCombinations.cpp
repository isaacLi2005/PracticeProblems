#include <bits/stdc++.h>
using namespace std;

const int MOD = 1'000'000'007;   // (10**9) + 7

// Faithful port of coinCombinations(x, coinsList)
void coinCombinations(int x, const vector<int>& coinsList) {
    vector<int> memo(x + 1, 0);
    memo[0] = 1;

    for (int target = 1; target <= x; ++target) {
        for (int coin : coinsList) {
            int remainder = target - coin;
            if (remainder >= 0) {
                memo[target] = (memo[target] + memo[remainder]) % MOD;
            }
        }
    }

    cout << memo[x] << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    if (!(cin >> n >> x)) return 0;

    // read coins, drop duplicates just as list(set(...)) does
    unordered_set<int> uniq;
    for (int i = 0; i < n; ++i) {
        int c;
        cin >> c;
        uniq.insert(c);
    }
    vector<int> coinsList(uniq.begin(), uniq.end());

    coinCombinations(x, coinsList);
    return 0;
}
