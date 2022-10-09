# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

while True:
    N = int(input())
    if 0 <= N & N <= 100: # N은 100보다 작거나 같은 자연수
        break

words = []
for _ in range(N): # 반복 수행하되 변수 값이 필요 없을 때 '언더바'
    words.append(input())

counter = 0 # 그룹단어 카운터
for w in words:
    check = []
    is_group = True
    arr = list(w) # 알파벳 하나씩 분리
    check.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]: # 중복 알파벳이 아닐 때
            if arr[i] in check: # 이전에 한번 나온 알파벳이면
                is_group = False # 그룹단어가 아님
                break
            else:               # 이전에 나온 알파벳이 아니면
                check.append(arr[i]) # 체크리스트에 새로 추가
    if is_group:
        counter += 1
    
print(counter)