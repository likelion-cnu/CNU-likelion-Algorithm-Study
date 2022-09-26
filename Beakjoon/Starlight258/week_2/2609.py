num = input().split()
x=int(num[0])
x1=x
y=int(num[1])
y1=y
r=0
#최대공약수 구하기-유클리드 호제법 이용
#Gcd(x, y) == Gcd(y, x%y) , x%y가 0일때 앞의 수가 최대공약수
while(y):
    r = x % y
    x= y 
    y= r 

print(x)
#최소공배수 구하기-유클리드 호제법 이용
#최소공배수는 두 수를 곱한 것을 최대공약수로 나눔
print(int(x1*y1/x))