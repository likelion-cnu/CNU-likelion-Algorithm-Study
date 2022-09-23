
num = int(input())

if 1<= num <= 10000000:
  sum= 2
  while True:
    for i in range(1,sum):
      now = '%d/%d'% (i , (sum-i))
      num=num-1
      print('test now', now, '& num',num)
      if (num==0):
        break
    if (num>0):
      sum=sum+1
    elif (num==0) :
      print(now)
      break
    else: 
      print('bug발생!')
      break
else : print('1과 10000000 사이의 수를 입력하십시오.')