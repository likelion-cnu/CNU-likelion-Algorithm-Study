
n= int(input())
if n<=100:
  gwlist=[]
  for _ in range(0,n):
    gwlist.append(input())
  # print(gwlist)

  result=0
  for gw in gwlist :
    have=[]
    palp=''
    group=True
    for alp in gw :
      if (alp==palp):continue
      elif (alp in have): 
        group=False
        break
      else: have.append(alp)
      palp=alp
    if (group): result=result+1
  print(result)

else: print('단어의 개수는 100개 이하여야 합니다. ')
