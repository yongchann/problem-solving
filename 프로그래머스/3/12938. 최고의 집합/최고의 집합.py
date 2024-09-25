def solution(n, s):
    base, remain = divmod(s, n)
    if base == 0:
        return [-1]
    
    return [base] * (n-remain) + [base + 1] * remain