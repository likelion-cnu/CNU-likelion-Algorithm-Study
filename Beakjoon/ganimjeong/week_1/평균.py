n = int(input()) 
orilist = list(map(int, input().split()))
M = max(orilist)
newlist =[]
for i in orilist:
    newlist.append(i/M*100)

average = sum(newlist)/n
print(average)