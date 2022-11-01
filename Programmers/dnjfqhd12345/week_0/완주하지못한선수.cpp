#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    vector<string> vec(1);

    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());

    set_difference(participant.begin(), participant.end(), completion.begin(), completion.end(), vec.begin());
    string answer = vec[0];

    return answer;
}