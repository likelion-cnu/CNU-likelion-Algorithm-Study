
### [Baekjoon-1157] 단어 공부

#알파벳으로 된 단어가 주어지고 대소문자로 구분하지 않음
word = (str(input())).upper()
cnt = []
word_list = list(set(word)) #중복을 제거하여 갯수를 카운트하여 cnt에 저장

for i in word_list:
  count = word.count(i)
  cnt.append(count)

#가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력
if cnt.count(max(cnt)) >= 2:
  print("?")

#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다
else:
  print(word_list[(cnt.index(max(cnt)))].upper())

#https://www.acmicpc.net/problem/1157