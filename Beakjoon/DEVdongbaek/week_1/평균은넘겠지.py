C = int(input())


for i in range(C):
    score = list(map(int,input().split(' ')))
    average = sum(score[1:]) / score[0] # score[0]은 학생 수, score[1:]는 점수 
    count = 0
    
    for j in score[1:]:
        if j > average: # 평균보다 높은 점수당 변수 + 1
            count += 1
    ans_aver = count / score[0] * 100 # 평균보다 높은 학생을 전체 학생수에서 백분율로 계산
    print("{:.3f}%".format(ans_aver))