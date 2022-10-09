# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

while True:
    N = int(input())
    if N <= 100:
        break

prime_count = 0
num_list = list(map(int, input().split()))

if len(num_list) == N: # 입력받은 N과 리스트 개수 같은지 비교
    for n in num_list:
        count = 0
        if n <= 1000: # 입력받은 리스트 요소가 1000 이하인지 비교
            for i in range(1, n+1):
                if n % i == 0:
                    count += 1
            if count == 2: # 1과 자기 자신으로만 나누어 떨어지면
                prime_count += 1 # 소수 카운터 1증가

print(prime_count)