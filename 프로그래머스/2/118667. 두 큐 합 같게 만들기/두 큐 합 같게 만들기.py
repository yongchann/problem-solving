def solution(queue1, queue2):
    q = queue1 + queue2
    target, remain = divmod(sum(q), 2)
    if remain != 0:
        return -1

    idx1, idx2, last = 0, len(queue1), len(q)
    curr = sum(q[:idx2])
    answer = 0   
    while True:
        if idx1 >= idx2 or idx2 == last:
            return -1
        
        if curr == target:
            return answer
        
        if curr < target:
            curr += q[idx2]
            idx2 += 1
            answer += 1
            
        elif curr > target:
            curr -= q[idx1]
            idx1 += 1
            answer += 1