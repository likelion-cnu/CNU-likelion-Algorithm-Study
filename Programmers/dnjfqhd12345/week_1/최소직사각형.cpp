#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int arrsize = sizes.size();
    for (int i = 0; i < arrsize; i++) {
        sort(sizes[i].begin(), sizes[i].end());
    }
    cout << sizes[0][0] << sizes[0][1] << endl;
    int min = sizes[0][0];
    int max = sizes[0][1];
    for (int i = 0; i < arrsize; i++) {
        if (sizes[i][0] >= min)
            min = sizes[i][0];
    }
    for (int i = 0; i < arrsize; i++) {
        if (sizes[i][1] >= max)
            max = sizes[i][1];
    }
    answer = min * max;
    return answer;
}