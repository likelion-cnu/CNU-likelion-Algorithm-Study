import sys

n=int(input())
score=[int(input()) for i in range(n)]
oavg=[]

avg = sum(score)/len(score)

for i in range(len(score)):
    if score[i] > avg:
        oavg.append(score[i])

reality = ((len(oavg))/(len(score))*100)
print(f"{reality:.3f}"+"%")
# print('{:.3%}'.reality)