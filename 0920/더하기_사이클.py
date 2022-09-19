
### [Baekjoon-1110] 더하기 사이클

N = 0

#0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 
while True:
  N = int(input())
  if(N<0)or(N>99):
    print(" -1<n<99 ")
    continue
  else:
    break
  
cycle = 0
input_N = N

while True:
  n1 = input_N % 10 #주어진 수의 가장 오른쪽 자리 수

  #앞에서 구한 합의 가장 오른쪽 자리 수
  n2 = input_N // 10
  sum_n = (n2+n1) % 10 
  
  #let x_1 is 26 such that 2+6=8 then x_2 has 68, so x_3;(6+8=14) to be 84
  input_N = (n1*10)+sum_n

  #how many cycle in function values be the same as input number
  cycle = cycle + 1 
  if(input_N == N):
    break

print("입력값의 사이클의 길이: ", cycle)
#https://www.acmicpc.net/problem/1110