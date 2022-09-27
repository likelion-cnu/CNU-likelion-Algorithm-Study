"""
대각선으로 줄을 나눠서 볼 수 있다.
1번째 줄 : [1/1]
2번째 줄 : [1/2, 2/1]
3번째 줄 : [3/1, 2/2, 1/3]
.
.
.

짝수라인은 증가할 수록 분자가 1씩 늘어나고, 분모가 1씩 감소한다.
ex) 2번째 줄 : 1/2 -> 2/1

홀수라인은 증가할 수록 분자가 1씩 줄어들고, 분모가 1씩 증가한다.
ex) 3번째 줄 : 3/1 -> 2/2 -> 1/3
"""

X = int(input())

line = 0 # 몇번째 라인인지
end = 0 # line의 마지막 인덱스

while X > end: # X가 마지막 인덱스에 도달할 때 까지
    line += 1 # X번째 숫자까지 라인의 숫자를 1씩 증가시킨다.
    end += line # 마지막 인덱스 = line!와 같다.


plus_minus = end - X # 마지막 인덱스에서 X 인덱스를 빼서 분자와 분모에 더하고, 빼줄 값을 만들어준다. 
     
     
if line % 2 == 0: # i가 2로 나누어 떨어질 때 
    a = line - plus_minus # 분자
    b = plus_minus + 1 # 분모
    
else: # i가 2로 나누어 떨어지지 않을 때
    a = plus_minus + 1 # 분자
    b = line - plus_minus # 분모
    
print(a,'/',b,sep='')