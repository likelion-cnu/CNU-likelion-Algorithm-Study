def solution(answers):
    pattern_1 = [1,2,3,4,5]
    pattern_2 = [2,1,2,3,2,4,2,5]
    pattern_3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt_arr = [0, 0, 0]
    
    answer = []
    
    for i in range(len(answers)):
        s1 = i % 5
        s2 = i % 8
        s3 = i % 10
        
        if pattern_1[s1] == answers[i]:
            cnt_arr[0] += 1
        if pattern_2[s2] == answers[i]:
            cnt_arr[1] += 1
        if pattern_3[s3] == answers[i]:
            cnt_arr[2] += 1

    
    
    # 일부 테스트케이스 부적합
    # if cnt_arr.count(max(cnt_arr)) >= 2:
    #     for i in range(len(cnt_arr)):
    #         if max(cnt_arr) == cnt_arr[i]:
    #             answer.append(i+1)       
    # else:     
    #     answer.append(cnt_arr.index(max(cnt_arr))+1)
    
    max_num = max(cnt_arr)
    
    
    for i in range(len(cnt_arr)):
        if cnt_arr[i] == max_num:
            answer.append(i+1)
            
    return answer

