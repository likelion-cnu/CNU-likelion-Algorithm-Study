N = 0
while True:
    try:
        N = int(input())
    except EOFError:
        break
cycle = 0
new_N = N # 처음 입력된 값에서 새롭게 변경된 값으로 할당
while True:
    N1 = new_N // 10
    N2 = new_N % 10
    sum_N = N1 + N2
    new_N = N2 * 10 + sum_N % 10

    cycle += 1
    
    if N == new_N:
        print(cycle)
        break