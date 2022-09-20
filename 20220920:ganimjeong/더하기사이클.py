ori=int(input ())
i=0
now=ori

while 1:
    a=now//10
    b=now%10
    c=(a+b)%10
    now= (b*10) + c
    i=i+1
    #print('횟수:',i,'/현재 숫자:',now)
    if (now==ori):
        break
print(i)