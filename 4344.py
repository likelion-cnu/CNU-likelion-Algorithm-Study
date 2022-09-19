for i in range(int(input())):
    li = list(map(int, input().split()))
    n = li[0]
    g_li = li[1:]
    average = sum(g_li)/n
    cnt = 0
    for g in g_li:
        if g > average:
            cnt += 1
    print('%.3f' %(cnt/n*100)+ '%')