a, b = map(int, input().split())


def gcd(a, b):  # 유클리드 호제법으로 최대공약수
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):  # 최소공배수
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))