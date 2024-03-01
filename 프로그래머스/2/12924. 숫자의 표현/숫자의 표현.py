def solution(n):
    answer = 0
    for i in range(1, n+1):
        add = i
        curr = 0
        while curr < n:
            curr += add
            add += 1
        
        if curr == n:
            answer += 1
            

    return answer