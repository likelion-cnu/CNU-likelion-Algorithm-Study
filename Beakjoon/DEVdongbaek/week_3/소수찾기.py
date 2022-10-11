N = int(input())

num = list(map(int, input().split(' ')))


for i in num:
    if i == 1: # 1은 소수가 아니기에 제외
        N -= 1
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            N -= 1
            break
        
        


print(N)
