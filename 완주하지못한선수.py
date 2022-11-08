# def solution(participant, completion):
#     part_dictionary = dict.fromkeys(participant,0)
#     comp_dictionary = dict.fromkeys(completion,0)
#     tmp = ''

#     for i in participant:
#         if participant.count(i) >= 2:
#             tmp = i

#     for k, v in part_dictionary.items():
#         if k in comp_dictionary:
#             if k == tmp:
#                 part_dictionary[k] += 2
#             else:
#                 part_dictionary[k] += 1
                
    
#     ans = []

#     for k, v in part_dictionary.items():
#         if v == 0 or v >= 2: 
#             ans.append(k)
    
#     return ans




def solution(participant, completion): # 해시 참고 -> https://ablue-1.tistory.com/68
    hashDict = {}
    sumHash = 0
    
    for part in participant:
        hashDict[part] = hash(part) # 딕셔너리의 key값으로는 참가자의 이름을, value 값으로는 이름의 해시값(랜덤한 숫자)을 저장한다.
        sumHash += hash(part) # 이름에 대한 해시값들을 저장한다.
    
    for comp in completion:
        sumHash -= hash(comp) # completion에 있는 참가자들의 해시값을 일일이 빼주면 결국 완주하지 못한 선수의 해시값만 남을 것이다
    
    
    for k, v in hashDict.items(): # 딕셔너리의 value가 위에서 구한 완주하지 못한 선수의 value와 같다면 해당 값을 리턴해줌.
        if v == sumHash:
            ans = k
            
    return ans
