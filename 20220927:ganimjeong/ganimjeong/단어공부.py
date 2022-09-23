# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서
# 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.


# 단, 대문자와 소문자를 구분하지 않는다.
# 입력 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.

word = input()
capword= word.upper()
# capword= word.capitalize()
# print(capword)

# 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

if len(word)<=1000000:

  wordlist=list(capword)
  worddict={}
  for i in wordlist:
    if i in worddict:
      worddict[i]=worddict[i]+1
    else: worddict[i] = 1
  
  maxkey=wordlist[0]
  # maxvalue=max(list(worddict.values))
  buglist=[]

  for key in worddict:
    if (worddict[key]>worddict[maxkey]):
      maxkey=key
      print('맥스 키를',maxkey,'로 변경')

    elif (worddict[key]==worddict[maxkey]):
      if (key==maxkey):continue
      else: 
        buglist.append(key)
        buglist.append(maxkey)
        print('buglist updated! : ', key, maxkey)

    elif (worddict[key]<worddict[maxkey]):
      continue


# 출력 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을
# 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


  if maxkey in buglist: print('?')
  else: print(maxkey)
  
else:print('1,000,000자 이내로 써주세요.')




