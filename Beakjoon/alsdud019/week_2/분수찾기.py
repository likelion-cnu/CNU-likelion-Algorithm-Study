num=int(input())

line=0
max_num=0

#입력값이 속한 사선라인의 라인수와 최댓값
while(num>max_num):
    line+=1
    max_num+=line

#입력값과 사선라인중 최댓값의 차이
gap=max_num-num

#사선라인이 짝수일 때 
if line%2==0:
    top=line-gap
    bottom=gap+1

#사선라인이 홀수일 때
else:
    top=gap+1
    bottom=line-gap

print(f'{top}/{bottom}')