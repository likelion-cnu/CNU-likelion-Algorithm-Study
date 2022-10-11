arr = list(map(int,input().split()))
a = int(arr[0])
b = int(arr[1])
small = 0 # a,b 중 작은 수
max = 1 # 최대공약수
min = 1 # 최소공배수를 구하기 위한 min 변수 (max*min = 최소공배수)
list1 = []  # 나누는 수를 담는 list1
list2 = []  # a,b를 계속 나눠 남는 수를 담는 list2

if a>b: # 어떤 수가 더 작은 수인지
    small=b
else:
    small=a

for i in range(0,1000000): # for 무한루프 구현
    count = 0 # 더이상 나누어 떨어지는지 아닌지 판별하는 변수 count가 0이면 더이상 나눠떨어지는 수가 없다고 판별한다.
    for i in range(2, small+1): # 2~small까지 반복
        if (a%i==0) and (b%i==0): # i가 a와 b로 나눠진다면
            a = a//i # a와 b를 i로 나눈 결과값을 저장
            b = b//i
            list1.append(i) # 나누는 수인 i를 list1에 담는다.
            small = small//i # 
            count +=1 # count 1 증가
            break # for문 탈출
        else: # 나눠떨어지지 않는다면
            continue # for문 continue
    if count!=0: # count가 0이 아니라면 continue
        continue
    list2.append(a) #  list2에 마지막으로 남은 a, b 값을 저장
    list2.append(b)
    break

for i in list1:
    max = max*i # 나누는 수를 모조리 곱한다. (최소공배수)

for i in list2:
    min = min*i # 마지막 남은 a, b값을 곱한다.

print(max) # 최대공약수 출력
print(max*min) # 최소공배수 출력