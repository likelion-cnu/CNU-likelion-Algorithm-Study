def d(n): #d(n) 함수
    n = n+sum(map(int, str(n))) 
    # sum(map(int, str(n)))을 이용해서 n의 각 자리 수를 문자형으로 변환하고, map으로 각 자리를 분리해준 후 분리 된 수들을 sum으로 더해줌!
    return n

# 생성자 탐색할 리스트의 크기 지정해주기
a = [0]*10001

# 생성자 탐색
for i in range(1, 10001):
        a[i] = d(i) # d(i)는 생성자 값이므로, a[i]도 생성자 값을 입력 받는다. 
        # 이는 아래서 셀프넘버를 구하기위해 사용된다
   

for i in range(1, 10001):
    if i not in a: #i가 생성자 값이 없으면, 즉 셀프 넘버이면 출력하라.
        print(i)