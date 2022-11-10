
### [Baekjoon-2609] 최대공약수와 최소공배수

#첫째 줄에는 두 개의 자연수가 주어지고 한 칸의 공백이 있다
a, b = map(int, input().split())

# 최대공약수 
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# 최소공배수
lcm = a * b // gcd(a, b)

print(gcd(a, b))
print(lcm)
#https://www.acmicpc.net/problem/2609