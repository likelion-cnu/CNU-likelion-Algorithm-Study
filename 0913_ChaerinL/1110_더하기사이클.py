# 1. num 입력받기
n = int(input())
i = 1

#새로운 수 구하기
m = (int(n % 10)*10+int((int(n/10)+int(n % 10)) % 10))

#while or for, 처음과 같으면 break
# for m=n:
#     num.append(m)

if n==0:
    print(1)
    
while m != n:
    m = (int(m % 10)*10+int((int(m/10)+int(m % 10)) % 10))
    i = i+1
    if m == n:
        print(i)
        break
