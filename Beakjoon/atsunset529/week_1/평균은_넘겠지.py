
### [Baekjoon-4344] 평균은 넘겠지

#첫째 줄에는 테스트 케이스의 개수 C
C = int(input())


#둘째 줄부터 각 테스트 케이스마다 1. 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고 2.이어서 N명의 점수(.append)
for i in range(C):
  score = list(map(int, input("학생 수 입력 후 점수입력:").split()))
  avg = sum(score[1:])/score[0]
  over_avg = 0
  
  for j in score[1:]:
    if j > avg:
      over_avg += 1
      
  #케이스마다 한 줄씩 평균을 넘는 학생들의 비율
  upper_mean = over_avg / score[0] * 100

  print("{:.3f}%".format(upper_mean))
  #https://www.acmicpc.net/problem/4344