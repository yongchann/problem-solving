
def solution(q1, q2):
    q = q1 + q2
    target = sum(q)//2
    answer = 0
    
    # 누적합 저장
    prefix_sum = [0] * (len(q)+1)
    for i in range(1, len(q)+1):
        prefix_sum[i] = prefix_sum[i-1] + q[i-1]
    
    # 두개의 포인터
    p1, p2 = 0, len(q)//2
    
    while True:
        if p1 >= p2 or p2 > len(q):
            answer = -1
            break
            
        diff = prefix_sum[p2] - prefix_sum[p1]
        
        if diff == target:
            break
        elif diff > target:
            p1 += 1
            answer += 1
        elif diff < target:
            p2 += 1
            answer += 1
            
    return answer
    
