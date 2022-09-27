n = int(input()) # N을 입력
cnt = 1 # 기본 count값 1로 cnt 변수 초기화

if n<10:
    new_num = '0'+str(n) # 10보다 작다면 앞에 0을 붙이기
    before_num = new_num # 입력 받은 수를 문자로 변환시키고 before_num 변수에 저장
    while True: 
        sum_num = int(before_num[0]) + int(before_num[1]) # 십의자리와 일의자리를 더함
        sum_num = str(sum_num) # 더한 결과를 문자로 변환시킨다.
        new_str = before_num[1] + sum_num.strip()[-1] # 입력받은 수와 더한 수의 일의자리를 합친다.
        if(new_str==new_num): # 사이클이 돌아왔으면 
            break # 끝낸다.
        else:
            cnt+=1 # 사이클이 끝나지 않으면 카운터 +1
            before_num=new_str # before_num 변수에 합쳤던 new_str 수로 할당

if n>=10:
    new_num = str(n)
    before_num = new_num # 입력 받은 수를 문자로 변환시키고 before_num 변수에 저장
    while True:
        sum_num = int(before_num[0]) + int(before_num[1]) # 십의자리와 일의자리를 더함
        sum_num = str(sum_num) # 더한 결과를 문자로 변환시킨다.
        new_str = before_num[1] + sum_num.strip()[-1] # 입력받은 수와 더한 수의 일의자리를 합친다.
        if(new_str==new_num): # 사이클이 돌아왔으면
            break # 끝낸다.
        else:
            cnt+=1 # 사이클이 끝나지 않으면 카운터 +1
            before_num=new_str # before_num 변수에 합쳤던 new_str 수로 할당

print(cnt) # 총 카운트된 수 출력