#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    int a;
    int b;
    int size;
    int idx;
    vector<int> copyarr;
    vector<int> answer;
    for (int i = 0; i < commands.size(); i++) {
        a = commands[i][0];
        b = commands[i][1];
        idx = commands[i][2];
        size = b - a + 1;
        for (int j = a; j <= b; j++) {
            copyarr.push_back(array[j-1]);
        }
        sort(copyarr.begin(), copyarr.end());
        answer.push_back(copyarr[idx-1]);
        copyarr.clear();
    }
    return answer;
}