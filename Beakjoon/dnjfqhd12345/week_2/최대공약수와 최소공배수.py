arr = list(map(int,input().split()))
a = int(arr[0])
b = int(arr[1])
small = 0 # a,b 중 작은 수
max = 1 # 최대공약수
min = 1 # 최소공배수
list1 = []  # 최대공약수를 담을 list1
list2 = []  # 최소공배수를 담을 list2

if a>b:
    small=b
else:
    small=a

for i in range(0,1000000):
    count = 0
    for i in range(2, small+1):
        if (a%i==0) and (b%i==0):
            a = a//i
            b = b//i
            list1.append(i)
            small = small//i
            count +=1
            break
        else:
            continue
    if count!=0:
        continue
    list2.append(a)
    list2.append(b)
    break

for i in list1:
    max = max*i

for i in list2:
    min = min*i

print(max)
print(max*min)