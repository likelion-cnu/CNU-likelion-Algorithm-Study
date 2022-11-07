
### [Baekjoon-1316] 그룹단어체커

cnt = 0
n = int(input())
#words = list(map(str, input().lower().split()))

for i in range(n):
  if n < 101:
    word = input()
    if list(word) == sorted(word, key=word.find): #only sorted: cbac->abcc, with .find->ccba
      cnt += 1
  else:
    print("n < 101")
    break

print(cnt)

#https://www.acmicpc.net/problem/1316