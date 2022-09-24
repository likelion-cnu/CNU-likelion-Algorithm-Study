sub = int(input())
scores = list(map(int, input().split(' ')))
M = max(scores) # 최댓값

new = [] 
for i in scores:
    new.append(i/M*100) # 점수/M*100
   
average = sum(new)/sub # 새로운 평균

print(average) 