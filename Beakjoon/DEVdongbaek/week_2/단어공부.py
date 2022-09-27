s = input().upper() # 대문자로 통일
s_list = list(set(s)) # 문자열중 중복 문자 제거 // 인덱스 번호로 사용하기 위해서
count = [] # 중복 횟수를 저장할 리스트

for i in s_list: # ex) s : z, Z, a -> s_list : Z, A -> count -> 2, 1
    cnt = s.count(i) # 중복 개수를 COUNT 리스트에 저장
    count.append(cnt)
    
if count.count(max(count)) >= 2: # count 리스트의 최대수가 1개 이상이면 '?' 출력
    print('?')
else:
    print(s_list[(count.index(max(count)))]) # 최대수를 가진 인덱스를 출력하라