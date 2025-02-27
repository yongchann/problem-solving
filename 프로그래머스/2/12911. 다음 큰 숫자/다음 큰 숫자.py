def solution(n):
    def get_cnt(k):
        return str(bin(k))[2:].count('1')
    
    cnt = get_cnt(n)
    target = n + 1
    while True:
        if get_cnt(target) == cnt:
            return target
        target += 1
        