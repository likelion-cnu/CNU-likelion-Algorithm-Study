from math import trunc


n = int(input())
m = n # 입력받은 n을 m으로 옮겨줌 -> 후 if문에 사용 하기위해서
plus = 0
new = 0
index = 0


while True:
    plus = (n%10) + (n//10) # 26 -> 6 + 2 = 8
    new = ((n%10)*10)+plus%10 # 합의 가장 오른쪽 자리 수
    index += 1
    n = new

    if new==m:
        break


print(index)
 