testCase=int(input("testCase:"))
result=[]
avgList=[]

def overavg(list):
    check=0
    print(list[0])
    hap=sum(list)-list[0]
    avg=hap/(len(list)-1)
    # print(avg)
    for i in range(1,len(list)):
        if list[i]>avg:
            check+=1
    return check
    

for i in range(testCase):
    avgList=list(map(int,input().split()))
    count=overavg(avgList)
    per=count/avgList[0]*100
    result.append(round(per,3))

for i in range(len(result)):
    print(result[i],"%\n")
# print(overavg(list))
    