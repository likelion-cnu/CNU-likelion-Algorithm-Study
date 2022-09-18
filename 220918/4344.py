#백준 4344번
caseNum=int(input()) #테스트 케이스 수
average=sum=highNum=answer=0 #초기화
for i in range(caseNum): #테스트 케이스 수 만큼 반복
    case=input().split()
    studentNum=int(case[0]) #학생 수
    for j in range(studentNum): #합 구하기
        sum+=int(case[j+1]) #총 점수 구하기
    average=sum/studentNum #평균 구하기
    for j in range(studentNum): #평균 넘는 학생들의 수 구하기
        if(average<int(case[j+1])):
            highNum+=1 
    answer = (highNum/studentNum)*100 #평균 넘는 학생들의 비율 구하기
    print('%.3f'%answer+'%') #소수점 셋째자리까지 출력
    sum=highNum=0 #초기화



