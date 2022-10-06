
### [Baekjoon-1978] 소수찾기

n = int(input())
data = list(map(int, input().split()))
prime_num = 0

if n == len(data): #첫줄 수의 갯수 n

  for i in data: #n개중 소수의 개수 구하기
      cnt = 0 
      if(i == 1): 
          continue
      for j in range(2, i+1):
          if(i % j == 0): #2~자신의 수까지 나누어떨어지는지
              cnt += 1 
      if(cnt == 1): #자신으로 나눈 하나만 나머지가 없었다면 소수
          prime_num += 1

  print(prime_num)  

else:
  print("첫번째 입력한 숫자를 확인하세요")

#https://www.acmicpc.net/problem/1978