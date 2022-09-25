n = int(input())
m = list(map(int, input().split()))
avg = 0

for i in range(n):
    avg += m[i] / max(m) * 100

print(avg / n)