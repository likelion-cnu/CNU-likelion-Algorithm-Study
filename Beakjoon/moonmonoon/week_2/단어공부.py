# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 
# 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 
# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

words = []
words = list(input().upper()) # 대문자로 변환하여 리스트 저장
# print(words)

check = list(set(words)) # 중복제거
# print(check)

num = [] # 각 문자별 개수 저장
for c in check:
    num.append(words.count(c))
# print(num)

i = num.index(max(num)) # num 리스트에서 가장 큰 값의 인덱스 반환
if num.count(max(num)) > 1: # max 값이 1개 초과라면 ? 출력
    print('?')
else:
    print(check[i])




