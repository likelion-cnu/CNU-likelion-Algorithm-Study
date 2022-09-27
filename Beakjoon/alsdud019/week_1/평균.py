def average(num,list):
    maximun=max(list)
    result=[]

    for i in range(0,len(list)):
        elem=list[i]/maximun*100
        result.append(elem)

    average=sum(result)/num
    return average


num=int(input("1000미만의 과목 개수를 입력:"))

num_list=list(map(int,input().split()))

print(average(num,num_list))