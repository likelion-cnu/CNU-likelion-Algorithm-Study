N = int(input())
cnt = 0


for i in range(N):
    a = input()
    err = 0
    for j in range(len(a)-1): # a문자열의 길이만큼 반복 
        if a[j] != a[j+1]: # 만약 a[j]와 a[j+1]이 같지않다면, 
            new = a[j+1:]    # a[j+1]부터 new 문자열에 옮겨준다.
            if new.count(a[j]) > 0: # 만약 new문자열에 a[j]가 나오면
                err += 1 # err를 1씩 올려준다.
    if err == 0: # 만약 err가 안나오면
        cnt += 1 # cnt를 1씩 올려준다.

print(cnt)