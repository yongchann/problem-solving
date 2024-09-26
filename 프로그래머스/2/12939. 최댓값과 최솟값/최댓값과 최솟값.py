def solution(s):
    n = list(map(int, s.split()))
    return str(min(n)) +' '+ str(max(n))
    