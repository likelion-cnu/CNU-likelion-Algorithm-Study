#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    // 최소의 길이를 먼저 구하기
    vector<string>::iterator it;
    sort(phone_book.begin(), phone_book.end(), less<string>()); // 정렬

    for (it = phone_book.begin(); it < phone_book.end()-1; it++) {
        if ((*(it+1)).find(*(it)) != string::npos) {
            answer = false;
            break;
        }
    }
    // 이거 작은 size vector에 저장해서 일일이 비교하면 될 것 같음!
    // 정렬하고 앞 뒤 비교하면 될 것 같음.

    return answer;
}