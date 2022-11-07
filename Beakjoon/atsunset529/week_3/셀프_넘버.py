
### [Baekjoon-4673] 셀프넘버


numbers = set(range(1, 10001))
non_selfnumbers = set()

#n을 d(n)의 생성자라 하고 셀프넘버는 생성자가 없는 숫자
#이때 dn은 수열; 33 + 3 + 3 = 39이고, 그 다음 수는 39 + 3 + 9 = 51
for d_n in numbers:
  for n in str(d_n):
    d_n += int(n)
  non_selfnumbers.add(d_n) #셀프넘버가 아닌 숫자를 집합에 추가

selfnum = numbers - non_selfnumbers #둘 다 집합이라 차집합 계산
print(sorted(selfnum)) #정렬
#https://www.acmicpc.net/problem/4673