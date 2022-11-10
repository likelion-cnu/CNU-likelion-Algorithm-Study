def solution(participant, completion):
    hash1 = {}
    hash2 = {}
    answer = ""

    for key in participant:
        if key in hash1:
            hash1[key] += 1
        else:
            hash1[key] = 1
    # print(hash1)

    for key in completion:
        if key in hash1:
            hash1[key] -= 1
    # print(hash1)

    for key in hash1:
        if hash1[key] != 0:
            answer = key

    return answer

# 100점!