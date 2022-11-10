
### [Baekjoon-1546] 평균

#첫째 줄에 시험 본 과목의 개수 N
N = int(input())
while True:
  if (N>1000):
    print("N<1001")
    continue
  else:
    break

#둘째 줄에 세준이의 현재 성적 +적어도 하나는 0점 아님+
score = list(map(int, input().split()))
M = max(score) #점수 중 최댓값

#모든 점수를 (점수/M*100)으로 고쳤다
for i in range(N):
  score[i] = score[i] / M * 100

print("새로운 평균은 %.2f 점" % (sum(score)/N))
#https://www.acmicpc.net/problem/1546