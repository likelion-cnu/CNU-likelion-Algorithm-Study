#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer(0);
    vector<int>::iterator it;
    int vecSize = progresses.size();
    int num = 0;

    for (;;) {
        vector<int>::iterator it = progresses.begin();
        vecSize = progresses.size();
        if (progresses.empty()) {
            break;
        }
        for (int i = 0; i < vecSize; i++) {
            progresses[i] += speeds[i];
        }

        if ( progresses[0]>= 100) {
            num++;
            progresses.erase(progresses.begin());
            speeds.erase(speeds.begin());

            for (; ; ) {
                if (progresses.empty())
                    break;
                if (progresses[0] >= 100) {

                    progresses.erase(progresses.begin());
                    speeds.erase(speeds.begin());
                    num++;
                }
                else {
                    break;
                }
            }
            if (num != 0) {
                answer.resize(answer.size());
                answer.push_back(num);
                num = 0;
            }
        }


    }
    return answer;
}