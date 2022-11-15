def solution(array, commands):
    arr = array # [1, 5, 2, 6, 3, 7, 4]
    answer = []
    for i in range(len(commands)):
        step_one_arr = arr[commands[i][0]-1:commands[i][1]] # [5, 2, 6, 3]
        print(step_one_arr)
        step_one_arr.sort() # 2, 3, 5, 6
        print(step_one_arr)
        answer.append(step_one_arr[commands[i][2]-1]) # 5 추가
    
    return answer

