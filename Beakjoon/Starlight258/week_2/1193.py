num = int(input())

line=0 #라인
end=0 #한 라인에서 최대값
while num>end: #라인 확인
    line+=1
    end+=line 

diff = end-num
if line%2 ==0: #사선 짝수번째
    top=line-diff #분자 
    under=diff+1        #분모
else: #사선 홀수번째
    top=diff+1 
    under=line-diff 

print(str(top)+"/"+str(under))