# def solution(phone_book): # 합계: 83.3 / 100.0
#     answer = True
#     phone_book.sort() # 119, 97674223, 1195524421
    
#     for i in range(len(phone_book)):
#         if i != 0:
#             for j in range(len(phone_book[i])): # 8
#                 phone = phone_book[i] # 97674223
#                 if phone_book[0] == phone[:j]:
#                     answer = False 
#                     break

#     return answer


def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1): # 0, 1
        if phone_book[i+1] is not None:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: # 접두어이기 때문에
                answer = False
                break
            
    return answer