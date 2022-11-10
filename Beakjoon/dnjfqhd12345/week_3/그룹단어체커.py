N = int(input())

# 카운트를 전체 단어 개수 N개에서 그룹 단어가 아닌 경우 하나씩 빼는 방식으로 접근
cnt = N
for i in range(N):
    word = input()
    for idx in range(len(word)-1):
        # idx를 기준으로 앞뒤 단어가 다를 경우
        if word[idx] != word[idx+1]:
            # idx 뒤쪽 인덱스의 문자열에서 word[idx+1] 문자가 포함되어 있는지 확인
            if word[idx+1] in word[:idx]:
                # 포함되어 있다면 그룹단어가 아니기 때문에 cnt 하나 감소
                cnt-=1
                break
print(cnt)