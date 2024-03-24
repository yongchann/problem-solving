from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([[numbers[0], 1], [-numbers[0], 1]])
    
    while q:
        value, cnt = q.popleft()
        if value == target and cnt == len(numbers):
            answer += 1
        else :
            if cnt < len(numbers):
                q.append([value + numbers[cnt], cnt+1])
                q.append([value - numbers[cnt], cnt+1])
    return answer
            
    
    
