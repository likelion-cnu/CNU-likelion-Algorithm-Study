selfnum =[] 
#좀 잘푼듯ㅋ 아님말고~
for _ in range(1,10001):
  selfnum.append(_) #일단 모든 숫자를 담아벌랑

for i in range (1,10001):
  num = i 
  while True:
    if i==0 : break #자릿수를 다 지워 사라지면 while문을 벗어납니다.
    num += i%10 #지금의 일의자릿수만 더해줍니다
    i = int(i/10) #자릿수 줄이기 -> 꼭 int를 붙여줘야 하더랍니다
  if num in selfnum:
    selfnum.remove(num)
    # print(num, '을 1~10000 리스트에서 지웁니다.')
  else: 
    # print(num, '은 한 번 지웠거나 10000을 넘은 수이기에 못지웁니다.')
    continue

for painter in selfnum:
  print(painter) #한 불씩 페인트해용
