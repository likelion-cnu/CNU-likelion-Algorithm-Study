# 백준 1110번
x = int(input()); #입력값
init=x #초기값 설정
first=second=0 #first=가장 오른쪽 자리 수, second=합의 가장 오른쪽 자리 수
cycle=0 #사이클 길이
if x==0: cycle=1 #0일때 예외처리
while(((int(init/10)!=first) or (init%10 !=second))): #init값과 first*10+second가 같지 않을동안
    cycle +=1 
    if(x<10): #주어진 수가 10보다 작을때
        first=x
        second=x 
        x=10*first+1*second 
    else:
        first=x%10
        second=(int(x/10)+x%10)%10  
        x=10*first + 1*second
    
print(cycle)

