def solution(citations):
    citations.sort()
    answer = 0
    
    # h : [0, len(citations)]
    for h in range(len(citations)+1):
        # h번 이상 인용된 논문의 첫 등장 위치 획득
        idx = -1
        for j, value in enumerate(citations):
            if value >= h: 
                idx = j
                break
                
        if idx < 0:
            break
            
        if len(citations) - idx >= h:
            answer = h
            
    return answer
    
