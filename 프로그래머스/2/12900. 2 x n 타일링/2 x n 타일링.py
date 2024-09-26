def solution(n):
    a, b = 1, 2
    for _ in range(2, n):
        b = a + b
        a = b - a
        
    return b % 1000000007