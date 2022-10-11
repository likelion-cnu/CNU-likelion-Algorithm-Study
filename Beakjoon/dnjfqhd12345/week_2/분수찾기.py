num = int(input()) # 숫자를 입력받는다.

lastIndex = 0 # 마지막 줄의 마지막 인덱스
lineNum = 0 # 몇번째 줄인지?

while lastIndex<num: # 몇번째 줄인지 마지막 인덱스가 몇인지 탐색
    lineNum += 1
    lastIndex += lineNum

diff = lastIndex - num # 마지막 줄의 마지막 인덱스와 입력한 숫자 차이
if lineNum%2==0: #짝수 번째 줄이면
    topNumber = lineNum - diff  # 분모 구하기
    bottomNumber = diff + 1 # 분자 구하기
else: # 홀수 번째 줄이면
    topNumber = diff + 1 # 분모 구하기
    bottomNumber = lineNum - diff # 분자 구하기

print(f'{topNumber}/{bottomNumber}') # 해당 인덱스 분수 출력