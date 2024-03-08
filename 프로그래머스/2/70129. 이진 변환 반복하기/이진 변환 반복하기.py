def solution(s):
    answer = [0, 0]
    while s != '1':
        cnt = s.count('0')
        s = s.replace('0','')
        
        answer[0] += 1
        answer[1] += cnt
        
        s = bin(len(s))[2:]
        
    return answer