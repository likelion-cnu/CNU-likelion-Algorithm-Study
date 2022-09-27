num = int(input()) # 숫자를 입력받는다.

lastIndex = 0
lineNum = 0

while lastIndex<num:
    lineNum += 1
    lastIndex += lineNum

diff = lastIndex - num
if lineNum%2==0: #짝수 번째 줄이면
    topNumber = lineNum - diff
    bottomNumber = diff + 1
else: # 홀수 번째 줄이면
    topNumber = diff + 1
    bottomNumber = lineNum - diff

print(f'{topNumber}/{bottomNumber}')