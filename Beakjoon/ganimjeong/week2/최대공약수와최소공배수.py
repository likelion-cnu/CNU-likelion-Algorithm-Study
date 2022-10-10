# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

a,b= map(int, input().split())
# print ('a:',a,'b:',b)

if (a<=10000) and (b<=10000):
  
    #최대 공약수
    aylist= []
    anb_ylist= []
    #약수 리스트 구하기
    for ay in range(1,a+1):
      if (a%ay==0):
        # print('a(',a,')약수리스트에 추가:',ay)
        aylist.append(ay)
      else:continue
    for by in aylist:
      if (b%by==0):
        # print('b(',b,')공통리스트에 추가:',by)
        anb_ylist.append(by)
      else: continue
    # print('a약수리스트:',aylist,'/ 공통리스트:',anb_ylist)

    cm_factor= max(anb_ylist)

    #최소 공배수
    ab= a/cm_factor
    bb= b/cm_factor

    cm_multiple = int(cm_factor*ab*bb)

    print(cm_factor)
    print(cm_multiple)

    

else : print('10,000이하의 자연수를 입력하세요.')
