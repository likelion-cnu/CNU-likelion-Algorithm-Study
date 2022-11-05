#[Programmers] 전화번호목록

def solution(phone_book):
  phone_book = sorted(phone_book) #문자로 정렬

  for i in range(len(phone_book)):
    for j in range(len(phone_book)):
      if i != j and phone_book[i].startswith(phone_book[j]): #i가 j로 시작하면 false출력
        return False

  return True

#https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3