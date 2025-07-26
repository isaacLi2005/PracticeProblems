#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b;
    if (!(cin >> a >> b)) return 0;

    vector<vector<int>> memo(a + 1, vector<int>(b + 1, -1));

    int limit = min(a, b);
    for (int i = 0; i <= limit; ++i) memo[i][i] = 0;

    const int INF = 1e9;

    for (int rows = 1; rows <= a; ++rows) {
        for (int cols = 1; cols <= b; ++cols) {
            if (rows == cols) continue;  

            int result = INF;

            for (int rowSplit = 1; rowSplit <= rows / 2; ++rowSplit) {
                int lowerHeight = rows - rowSplit;
                int cand = memo[rowSplit][cols] + memo[lowerHeight][cols];
                if (cand < result) result = cand;
            }

            for (int colSplit = 1; colSplit <= cols / 2; ++colSplit) {
                int leftWidth = cols - colSplit;
                int cand = memo[rows][colSplit] + memo[rows][leftWidth];
                if (cand < result) result = cand;
            }

            memo[rows][cols] = result + 1;     
        }
    }

    cout << memo[a][b] << '\n';
    return 0;
}
