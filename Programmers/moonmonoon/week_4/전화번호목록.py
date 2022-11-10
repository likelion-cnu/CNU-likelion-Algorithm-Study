def solution(phone_book):
    answer = True
    hash = {}

    for key in range(len(phone_book)):
        hash[key] = phone_book[key]

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if hash[j].find(hash[i]) == 0:
                answer = False
            if hash[i].find(hash[j]) == 0:
                answer = False

            # a = phone_book[i]
            # b = phone_book[j]
            # if len(a) >= len(b):
            #     if a[:len(b)] == b:
            #         answer = False
            # else:
            #     if b[:len(a)] == a:
            #         answer = False

    return answer

# 효율성 테스트 실패...