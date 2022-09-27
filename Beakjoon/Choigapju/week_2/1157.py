word = input().upper()  # 단어를 입력받고 upper를 통해 대문자로 변환
words = list(set(word))  # 리스트를 set으로 중복 제거
cnt = []

for i in words:  # words에 들어있는 각 문자들을 for문으로 반복
    count = word.count  # word에 입력된 단어에서 각 문자들이 몇 개씩 있는지 count
    cnt.append(count(i))  # cnt 변수에 append를 통해 count한 수를 입력

if cnt.count(max(cnt)) > 1:
    print("?")  # count한 값중 max값이 2개 이상 동일할 경우 ? 출력

else:
    print(words[(cnt.index(max(cnt)))])  # 가장 많이 count된 문자 출력