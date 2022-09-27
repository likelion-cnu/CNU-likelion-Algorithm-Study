#시험을 본 개수
num = int(input())


score_list = list(map(int,input().split()))


#최고점
max = int(score_list[0])

#최고점 추출
for i in range(0,num):
    if max < int(score_list[i]):
        max = int(score_list[i])


# 조작된 점수의 배열
new_scrlist=[]
# 조작된 점수의 구하기
for i in range(0,num):
    new_scr = int(score_list[i])/max*100
    new_scrlist.append(new_scr)

sum=0
# 조작된 점수의 평균 구하기
for i in new_scrlist:
    sum += i

avg = sum/num

print(avg)