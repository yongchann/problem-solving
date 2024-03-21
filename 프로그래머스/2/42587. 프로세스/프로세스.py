from collections import deque
def solution(priorities, location):
    priorities = deque(zip(range(len(priorities)), priorities))
    answer = 0
    while priorities:
        max_priority = max(list(zip(*priorities))[1])
        p = priorities.popleft()
        if p[1] == max_priority:
            answer += 1
            if p[0] == location:
                break
            else:
                continue
        else:
            priorities.append(p)
        
    
    return answer
    
