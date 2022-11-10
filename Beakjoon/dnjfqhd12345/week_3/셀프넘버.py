# 전체 숫자 집합을 생성합니다.
numbers = set(range(1,10000))
remove_set = set()

# 생성자인 숫자 remove_set에 담습니다.
for num in numbers:
    for n in str(num):
        num+=int(n)
    remove_set.add(num)

# 전체 숫자에서 remove_set을 지우고 정렬해서 출력합니다.
self_numbers = numbers-remove_set
for self_num in sorted(self_numbers):
    print(self_num)