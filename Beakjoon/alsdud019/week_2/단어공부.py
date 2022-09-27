word=input().lower()

Alphabet='abcdefghijklmnopqrstuvwxyz'

freq=[0]*26

#freq리스트에 해당 알파벳 수 증가
for i in word:
    if i in Alphabet:
        idx=Alphabet.find(i)
        freq[idx]+=1

#최대알파벳이 2개 이상일 경우 '?'출력
m=max(freq)
list=[i for i, v in enumerate(freq) if v==m]
if len(list)>1:
    print("?")
#freq리스트에 최대값에 해당하는 인덱스를 알파벳순과 비교하여 해당 알파벳을 대문자로 출력
else:
    max_idx=freq.index(max(freq))
    result=Alphabet[max_idx].upper()
    print(result)




# print(freq)

