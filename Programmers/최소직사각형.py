"""
모든 명함을 수납할 수 있는 가장 작은 지갑

명함의 가로, 세로의 최대값을 담아야 한다
BUT 명함을 돌릴 수 있음

1. 가로, 세로 둘 중 더 큰값을 big_arr에 저장하고, 더 작은 값을 sm_arr에 저장한다.
2. big_arr에서 제일 큰 값과 sm_arr서 제일 큰 값을 곱한다.
"""

def solution(sizes):
    big_arr = []
    sm_arr = []
    answer = 0
    
    for i in sizes: # [[60, 50], [30, 70], [60, 30], [80, 40]]
        big_arr.append(max(i)) #[60, 70, 60, 80]   
        sm_arr.append(min(i)) #[50, 30, 30, 40]
        
        answer = max(big_arr) * max(sm_arr)

    return answer