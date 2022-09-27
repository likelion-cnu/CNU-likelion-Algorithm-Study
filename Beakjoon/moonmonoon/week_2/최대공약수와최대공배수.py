# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 유클리드(Euclidean) 공식 이용
#   - 큰 수 A를 작은 수 B로 나누어 떨어지면, A, B의 최대공약수는 B
#   - A를 B로 나누었을 때 나머지가 R이면, A, B의 최대공약수는 R과 B의 최대공약수와 같다.
#   ex) GCM(15,12) = GCM(12,3)

# 유클리드 공식 이용 알고리즘 순서
# a. 두 수 A, B 중 큰 수, 작은 수를 판별한다.
# b. 큰 수를 작은 수로 나누어 나머지를 구한다.
# if 나머지가 0 : 작은 수가 최대공약수
# if 나머지가 0이 아니면 : 나누기 반복

# 최소공배수 구하는 알고리즘
# 최소공배수(LCM) = A x B / 최대공약수(GCD) 
# - 최대공약수를 구하고 A x B / GCD

n1, n2 = map(int, input().split())

a = n1
b = n2 # 원본값 저장

if a > b:
    while b > 0:
        a, b = b, a % b
    gcd = a
else:
    while a > 0:
        b, a = a, b % a
    gcd = b

lcm = n1 * n2 / gcd

print(gcd)
print(int(lcm))