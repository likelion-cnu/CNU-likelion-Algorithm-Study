N = 0
score = []
i = 0

N = int(input())
score = list(map(int, input().split()))


M = max(score)
for s in score:
    index = score.index(s)
    score[index] = s/M*100

avg = sum(score)/len(score)
print(avg)