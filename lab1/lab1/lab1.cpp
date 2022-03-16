#include <iostream>
#include <vector>

#define m 4

void combNoRep(std::vector<int> currentLevel, std::vector<int> combination, int level) {
    if (level == m) {
        bool print = true;
        for (int i = 0; i < combination.size(); i++) {
            if (i < combination.size() - 1 && combination[i] > combination[i + 1]) {
                print = false;
            }
        }
        if (print) {
            for (const auto& element : combination) {
                std::cout << element;
            }
            std::cout << "\n";
        }
    }
    else {
        for (int i = 0; i < currentLevel.size(); i++) {
            std::vector<int> tempCombination = combination;
            tempCombination.push_back(currentLevel.at(i));

            std::vector<int> nextLevel = currentLevel;
            nextLevel.erase(nextLevel.begin() + i);

            combNoRep(nextLevel, tempCombination, level + 1);
        }
    }
}

int main() {
    std::vector<int> input{ 1,2,3,4,5,6 };
    std::vector<int> emptyCombination{};
    combNoRep(input, emptyCombination, 0);
    return 0;
}