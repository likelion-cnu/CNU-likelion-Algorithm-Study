data = int(input())
for j in range(data):
    n = list(map(int, input().split())) #데이타 한 줄 값을 리스트로 집어넣어용
    average = sum(n[1:])/n[0] #그 줄의 평균 구함여
    ddokddok2 = 0
    for i in n[1:]:
        if i > average:
            ddokddok2 += 1  #평균넘어인간들을 똑똑이갯수에 추가
    result = ddokddok2/n[0] *100 #똑똑이비율 산출
    print(result)
