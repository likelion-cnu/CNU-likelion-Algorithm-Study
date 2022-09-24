A, B = map(int, input().split())


def GCD(A, B): # 유클리드 호제법을 이용해 최대공약수 구하기
    while B > 0:
        tmp = A
        A = B 
        B = tmp % B
    return A

# 두 자연수의 곱 = 최대공약수 X 최소공배수
# 최소공배수 = 두 자연수의 곱 / 최대 공약수

def LCM(A, B): # 최대공약수를 이용해 최소공배수 구하기
    return A * B / GCD(A, B)

print(GCD(A,B))
print(int(LCM(A,B)))
