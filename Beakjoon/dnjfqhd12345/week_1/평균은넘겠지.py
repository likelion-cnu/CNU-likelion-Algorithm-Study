num_test = int(input()) # 테스트 케이스 개수 입력

result_list=[] # 각 테스트 케이스 별 결과값 (비율)
cnt=0 # 평균 넘는 학생의 카운터

def avg_cal(list, num): # 평균을 구하기 위한 함수
    sum=0.0 
    for i in list:
        sum+=int(i) 

    avg = float(sum/num)
    return avg # 평균 반환


for i in range(0,num_test):
    cnt=0
    score_list = list(map(int,input().split()))
    num_input = int(score_list[0])
    avg = avg_cal(score_list[1:], num_input)

    for j in score_list[1:]:
        if j > avg:
            cnt= cnt+1
    percent = float((cnt/num_input)*100)
    result_list.append(percent)

for i in result_list:
    print("{:.3f}%".format(i))