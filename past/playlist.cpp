#include <iostream>
#include <unordered_set>
#include <algorithm>
#include <vector>

int main() {
    size_t n {};
    std::cin >> n;

    std::vector<int> playlist(n);
    for (size_t i {0}; i < n; i++) {
        std::cin >> playlist[i];
    }
    

    size_t startPointer {0};
    size_t endPointer {0};
    size_t bestSoFar {1};
    std::unordered_set<int> seenSongs {playlist[0]};
    seenSongs.reserve(200000);
    
    int nextSongToConsider {};
    while (endPointer < n - 1) {
        nextSongToConsider = playlist[endPointer + 1];
        if (seenSongs.find(nextSongToConsider) == seenSongs.end()) {
            seenSongs.insert(nextSongToConsider);
            endPointer++;
            bestSoFar = std::max(bestSoFar, seenSongs.size());
        } else {
            while (seenSongs.find(nextSongToConsider) != seenSongs.end()) {
                seenSongs.erase(playlist[startPointer]);
                startPointer++;
            }
        }
    }

    std::cout << bestSoFar << std::endl;


    return 0;
}