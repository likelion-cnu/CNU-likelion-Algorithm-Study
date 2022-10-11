words = str(input()) # 단어를 입력받는다.
words_list = list(words) # 입력된 단어를 리스트에 담는다.

words_dic = {} # 딕셔너리를 선언한다.

for i in words: # for문을 이용해서 만약 아스키코드가 대문자면 소문자로 바꿔준다.
    if(97<=ord(i)<=122):
        j=ord(i)-32
        i=chr(j)

    if(words_dic.get(i) == None): # 처음으로 카운트하는 알파벳이 있다면
        words_dic[i] = 1 # 해당 아스키코드값과 개수 1로 초기화
    else: # 이미 카운트 했던 알파벳이 있다면
        words_dic[i] += 1 # 해당 개수에서 +1

max = 0 # 가장 많이 사용된 알파벳 개수 초기화
for key,value in words_dic.items(): # 딕셔너리에 하나씩 꺼내면서 가장 많이 사용한 알파벳 찾기
    if max<value:
        max = value

same=0 # 최대값이 여러개 있을 경우를 판별하기 위한 same 변수

for key,value in words_dic.items(): # 최대값을 가진 key값이 몇개인지 탐색
    if value==max:
        same +=1

if same>=2: # 최대값이 2개이상 같다면
    print('?') # ? 출력
    quit()

for key,value in words_dic.items(): # 최대값이 1개로 유일하다면 key값 출력
    if value==max:
        print(key)