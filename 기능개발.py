def solution(progresses, speeds):
    answer = []
    
    """
    
    배포는 하루에 한번
    뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
    각 배포마다 몇개의 기능이 배포되는지 return

    progress = 93, 30, 55    



    speeds = 1, 30, 5,
    
    return 2, 1
    
    93은 7일 걸림 if ready 상태 변수가 있다면 더해주어서 함께 ans 리스트에 저장하기
    30은 3일 걸림 but 93이 완성 안되어있기에 93과 함께 배포 아마 ready 상태 변수에 +1 시켜놓으면 될듯
    55는 9일 걸림 
    
    
    progress = 95, 90, 99, 99, 80, 99 
    speeds = 1, 1, 1, 1, 1, 1
    
    return 1, 3, 2
    
    95는 5일 걸림 -> 5일째 완성
    90은 10일 걸림 -> 10일 걸림
    99는 1일 걸림 -> 90일짜리 기다렸다가 함께 완성
    99는 1일 걸림 -> 90일짜리 기다렸다가 함께 완성
    80일은 20일 걸림 -> 20일 완성
    99일은 1일 걸림 -> 80일짜리 기다렸다가 함께 완성
    
    """
    
    answer = [] # 결과를 담을 리스트
    time = 0 # 작업까지 걸린 시간
    worked = 0 # 이전 완료된 작업

    
    while len(progresses) > 0: # 작업 리스트가 빌 때까지 반복
        if (progresses[0] + speeds[0] * time) >= 100: # 작업이 완료된 경우 작업 완료 횟수 1을 증가시킨다.
            progresses.pop(0) # FIFO
            speeds.pop(0)   
            worked += 1 
        
        else: # 작업이 완료 되지않은 경우 
            if worked > 0: # 만약 완료된 이전 작업이 있다면 정답 리스트에 추가
                answer.append(worked)    
                worked = 0
            
            time += 1 # 작업에 걸리는 시간을 계속 더해준다.
    
    answer.append(worked) # 마지막 작업은 else문을 안거치기에 answer에 직접 추가해줌
    return answer


