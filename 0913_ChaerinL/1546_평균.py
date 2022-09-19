#2번
import sys

n = int(input("입력: "))
data = [int(input()) for i in range(n)]
ndata = []

for i in range(n):
    ndata.append(data[i]/max(data)*100)

print(sum(ndata)/len(ndata))

# 런타임에러....:)

#초기생각...
# 값 입력받기
# 제일 높은 수 찾기
# 나누기 n
# for로 n번만큼 돌리고 점수 누적
