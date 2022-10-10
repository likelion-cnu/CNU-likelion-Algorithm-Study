n = int(input())
if (n <=100) :
  numlist = list (map(int, input().split()))
  # print(numlist)
  if (len(numlist)==n):
    sosugeasu=0
    for num in numlist:
      for i in range(2,num):
        if (num%i==0):break
        if (i==(num-1)):sosugeasu=sosugeasu+1
    print(sosugeasu)

  else: print ('처음 입력하신 개수 만큼의 숫자를 집어넣어주세요.')
else: print('100개 이하의 수를 집어넣어주세요.')
