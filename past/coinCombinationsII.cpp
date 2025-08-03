#include <bits/stdc++.h>
using namespace std;

int main() {
    const int MOD = 1'000'000'007;

    int n;
    int x;
    cin >> n >> x;

    vector<int> coins(n);
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    vector<int> memo(x+1, 0);
    memo[0] = 1;

    for (int i = 0; i < n; i++) {
        int coin = coins[i];
        for (int target = 1; target <= x; target++) {
            int priorSum = target - coin;
            if (priorSum >= 0) {
                int priorWays = memo[priorSum];
                memo[target] = ((memo[target] % MOD) + (priorWays % MOD)) % MOD;
            }
        }
    }

    cout << memo[x] << "\n";



    return 0;
}