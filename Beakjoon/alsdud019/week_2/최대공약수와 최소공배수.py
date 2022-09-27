num1,num2=map(int,input().split())

#최대공약수 
for i in range(min(num1,num2),0,-1):
    if num1%i==0 and num2%i==0:
        print(i)
        GCD=i
        break

#유클리드호제법으로 최소공배수 구하기
LCM=(num1*num2)//GCD
print(LCM)
