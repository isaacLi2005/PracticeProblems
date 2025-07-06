#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    int m; 
    int k;

    std::cin >> n >> m >> k;


    std::vector<int> applicants(n);
    for (int i = 0; i < n; i++) {
        std::cin >> applicants[i];
    }
    std::sort(applicants.begin(), applicants.end());

    std::vector<int> apartments(m);
    for (int j = 0; j < m; j++) {
        std::cin >> apartments[j];
    }
    std::sort(apartments.begin(), apartments.end());


    int placed {0};
    int currentApplicant {0};
    int currentApartment {0};
    int apartmentSize {};
    int applicantSize {};
    while (currentApplicant < n and currentApartment < m) {
        apartmentSize = apartments[currentApartment];
        applicantSize = applicants[currentApplicant];

        if (applicantSize - k <= apartmentSize
            and apartmentSize <= applicantSize + k) {
            placed++;
            currentApplicant++;
            currentApartment++;
        } else if (applicantSize - k < apartmentSize) {
            currentApplicant ++;
        } else if (applicantSize + k > apartmentSize) {
            currentApartment++;
        }
    }

    std::cout << placed << "\n";

    return 0;
}