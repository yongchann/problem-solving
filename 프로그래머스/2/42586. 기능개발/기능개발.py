from collections import deque
def solution(progresses, speeds):
    answer = []
    
    p_list = deque(map(list, zip(progresses, speeds)))
    while p_list:
        if p_list[0][0] < 100:
            for i in range(len(p_list)):
                p_list[i][0] += p_list[i][1]
        
        cnt = 0
        while p_list and p_list[0][0] >= 100:
            cnt += 1
            p_list.popleft()
        
        if cnt:
            answer.append(cnt)
            
    return answer
            
                  
