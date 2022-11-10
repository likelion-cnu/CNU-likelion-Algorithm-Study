word = input().upper(); #대문자로 
unique = list(set(word)) #중복없는 문자 리스트

countList = [] #빈도수 리스트

for i in unique: #문자수만큼 쪼개기
    cnt = word.count(i) #빈도수
    countList.append(cnt)

if countList.count(max(countList)) >1: #max 빈도수가 여러개이면
    maxword='?'
else:
    m = countList.index(max(countList)) #max 인덱스 찾기
    maxword = unique[m]

print(maxword)