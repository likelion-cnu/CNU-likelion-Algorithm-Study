n = int(input())
cnt = n
for i in range(n):
    word = input().lower()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1:]:
            cnt -= 1
            break

print(cnt)

"""
그룹 단어 개수 최대 n개. cnt에 n 할당
반복문을 통해 현재의 알파벳이 다음 알파벳과 동일할 경우 계속해서 진행, 현재 알파벳이 다음 알파벳 이후에
존재시 cnt 값을 1 감소.
이를 반복 수행한 최종 결과 값을 cnt로 출력한다.
"""