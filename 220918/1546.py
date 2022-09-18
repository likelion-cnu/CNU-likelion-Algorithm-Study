# 백준 1546번
num=int(input()) #과목 수 
scores = input().split() #과목 점수 string 배열
max=sum=0 #최대값 max, sum 초기화
for i in scores: #최대값 구하기
    if(int(i)>max):
        max=int(i)
for i in scores: #점수 수정 후 합 구하기
    sum += (int(i)/max)*100
average=sum/num #평균 구하기  
print(average)



