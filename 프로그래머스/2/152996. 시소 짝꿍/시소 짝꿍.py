from collections import Counter

def solution(weights):
    answer = 0
    c = Counter(weights)

    for i in c:
        answer += c[i] * (c[i]-1) / 2
        answer += c[i] * c[i * 3/2]
        answer += c[i] * c[i * 4/3]
        answer += c[i] * c[i * 2]
        
    return answer
