#include <string>
#include <vector>
#include <iostream>

using namespace std;

void multiple(int num, vector<int> &stu1, vector<int> &stu2, vector<int> &stu3) {
    vector<int> stu1cpy; // 학생 1,2,3 복사배열 생성 (최소공배수 개수만큼 맞추기 위해)
    vector<int> stu2cpy;
    vector<int> stu3cpy;
    for (int k = 0; k < num; k++) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 5; j++) {
                stu1cpy.push_back(stu1[j]);
            }
        }
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 8; j++) {
                stu2cpy.push_back(stu2[j]);
            }
        }
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 10; j++) {
                stu3cpy.push_back(stu3[j]);
            }
        }
    }
    stu1 = stu1cpy; // 복사배열을 다시 원래 배열에 대입하기
    stu2 = stu2cpy;
    stu3 = stu3cpy;
}

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int>::iterator it;
    vector<int> stu1 = { 1,2,3,4,5 };
    vector<int> stu2 = { 2,1,2,3,2,4,2,5 };
    vector<int> stu3 = { 3,3,1,1,2,2,4,4,5,5 };
    int stu1ans = 0;
    int stu2ans = 0;
    int stu3ans = 0;
    int num = answers.size();
    int rest = (num / 40) + 1; // 최소공배수는 40이기 때문에 문제 개수에 따라서 얼마나 더 반복해야하는지를 위한 변수
    multiple(rest, stu1, stu2, stu3); // 학생들마다 사이클마다 번호 개수의 최소공배수로 3 학생들의 문제 푼 개수 맞추기


    for (int i = 0; i < num; i++) { // 답이 맞을 때마다 변수 값 증가
        if (stu1[i] == answers[i]) {
            stu1ans++;
        }
        if (stu2[i] == answers[i]) {
            stu2ans++;
        }
        if (stu3[i] == answers[i]) {
            stu3ans++;
        }
    }

    int max = stu1ans; // 고득점 구하기
    if (max < stu2ans) {
        max = stu2ans;
    }
    if (max < stu3ans) {
        max = stu3ans;
    }

    if (stu1ans == max) // 오름차순으로 고득점자 answer vector 정렬
        answer.push_back(1);
    if (stu2ans == max)
        answer.push_back(2);
    if (stu3ans == max)
        answer.push_back(3);



    return answer;
}