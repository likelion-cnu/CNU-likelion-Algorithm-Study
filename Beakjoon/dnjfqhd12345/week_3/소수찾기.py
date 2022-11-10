N = int(input())
n_list = list(map(int, input().split())) # 입력한 수를 공백 제거한 뒤 list에 저장

cnt = 0
for n in n_list: # 리스트에 있는 숫자를 하나하나 꺼내기
    if n != 1: # 1은 소수가 아님
        for i in range(2, n): # 2부터 n-1까지 나눠서 소수이면 cnt 증가 
            if n%i == 0:
                break
            else:
                cnt += 1

print(cnt) # 개수 출력해주기