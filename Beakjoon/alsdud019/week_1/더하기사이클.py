def digitcycle(num):
    if num<10:
        left=0
    else:
        left=num//10 #5
    right=num%10 #5
    hap=left+right #10
    if hap>=10:
        hap=hap%10 #0

    new=right*10+hap

    return new

check_num=1
newnum=0

num=int(input("숫자입력:"))

new_num=digitcycle(num)
# print(new_num)
while new_num!=num:
    check_num+=1
    new_num=digitcycle(new_num)
    # print(new_num)

print(check_num)

# print(digitcycle(num))

