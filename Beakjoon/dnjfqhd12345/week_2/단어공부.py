words = str(input()) # 단어를 입력받는다.
words_list = list(words)

words_dic = {}

for i in words:
    if(97<=ord(i)<=122):
        j=ord(i)-32
        i=chr(j)

    if(words_dic.get(i) == None):
        words_dic[i] = 1
    else:
        words_dic[i] += 1

max = 0
for key,value in words_dic.items():
    if max<value:
        max = value

same=0

for key,value in words_dic.items():
    if value==max:
        same +=1

if same>=2:
    print('?')
    quit()

for key,value in words_dic.items():
    if value==max:
        print(key)