#include <iostream>
#include <vector>
#include <algorithm>

int collectNumbers(size_t n, std::vector<int>& pos) {
    int rounds = 1;
    for (int i = 2; i <= n; i++) {
        if (pos[i] < pos[i - 1]) rounds++;
    }
    return rounds;
}

int broken(int v, std::vector<int>& pos) {
    // 1 if the pair is broken, 0 otherwise
    return (v >= 1 && v < pos.size() && pos[v] > pos[v+1]);
}

int main() {
    size_t n {}, m {};
    std::cin >> n >> m;

    int temp {};

    std::vector<int> pos(n + 1);
    std::vector<int> number(n+1);
    for (size_t i = 0; i < n; i++) {
        std::cin >> temp;
        pos[temp] = i + 1;
        number[i+1] = temp;
    }

    int rounds {collectNumbers(n, pos)};
    for (size_t i = 0; i < m; i++) {
        int a {}, b {};
        int aPos {}, bPos {};

        std::cin >> aPos >> bPos;
        a = number[aPos];
        b = number[bPos];
        bool consecutive = (a == b + 1) || (b == a + 1);

        rounds -= broken(a - 1, pos) + broken(a, pos) + broken(b - 1, pos) + broken(b, pos);
        if (consecutive) {
            // we subtracted the duplicate once too many – put it back
            rounds += broken(b == a + 1 ? a : b, pos);
        }

        std::swap(number[aPos], number[bPos]);
        pos[a] = bPos;  pos[b] = aPos;

        rounds += broken(a - 1, pos) + broken(a, pos) + broken(b - 1, pos) + broken(b, pos);
        if (consecutive) {
            rounds -= broken(b == a + 1 ? a : b, pos);
        }

        std::cout << rounds << std::endl;

        
        

    }

    return 0;
}