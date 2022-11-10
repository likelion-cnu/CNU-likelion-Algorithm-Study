"""
짝수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 늘어가고 분모가 1씩 감소하며

홀수라인은 시작점에서 끝점으로 갈수록 분자가 1씩 줄어들고 분모가 1씩 늘어난다.
"""
x = int(input())
line = 1

while x > line:             #n -= line을 하면 각 line에서 n이 몇번째에 위치하는지 알 수 있다.
    x -= line               #line이 짝수일때와 홀수일때 분모 분자의 증감 양상이 다르다.
    line += 1               #짝수일때는 분모 -1씩 분자 +1씩, 홀수일때는 분모 +1씩 분자 -1씩 증감한다.

if line % 2 == 0:
    up = x
    down = line - x + 1

else:
    up = line - x + 1
    down = x

print(up, '/', down, sep="")  #sep는 구분자로 print문에서 사용된다. 기본은 공백이다.