#[Programmers] 완주하지못한선수

def solution(participant, completion):
    participant = sorted(participant) #['filipa', 'josipa', 'marina', 'nikola', 'vinko']
    completion = sorted(completion) #['filipa', 'josipa', 'marina', 'nikola']

    for i in range(len(completion)):
        if participant[i] != completion[i]: #예시는 지금 이경우 없음
            answer = participant[i]
            return answer

    answer = participant[-1] #없으면 리스트 마지막인 vinko출력
    return answer

#https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3#

