def selfNum(n):
    num = n
    for i in list(str(n)):  # 예로 33이 들어오면 33을 리스트로 쪼개 [3, 3]으로 만들고 33 + 3 + 3으로 계산
        num += int(i)
    return num  # 반환


arr = []  # 셀프 넘버가 아닌 숫자 담는 array

for i in range(10000):
    arr.append(selfNum(i))  # 10000까지의 숫자중 셀프 넘버가 아닌 숫자 추가

for j in range(10000):
    if j in arr:
        pass  # j에 arr랑 같은 값이 있으면 pass
    else:
        print(j)  # 없으면 셀프 넘버이므로 출력