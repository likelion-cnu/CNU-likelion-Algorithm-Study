n = int(input()) // 입력받을
정수
개수
m = list(map(int, input().split())) // 정수
입력
pn = 0 // 소수개수
초기화

for i in m:
    if i == 1:
        continue // 소수가
        1
        일경우
        무시하고
        진행
    for j in range(2, i + 1):     //
    함수
    j는
    2
    부터
    1
    씩
    더하며
    반복문
    실행
    if i % j == 0:
        if j == i:
            pn += 1 // i를 j로 나눈 값이 0이면서 i와 j가 같으면 소수 개수 추가
            break

print(pn)