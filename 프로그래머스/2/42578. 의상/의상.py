from collections import defaultdict

def solution(clothes):
    my_clothes = defaultdict(list)
    for c in clothes:
        my_clothes[c[1]].append(c[0])
        
    answer = 1
    for _, v in my_clothes.items():
        answer *= (len(v)+1)
    
    return answer-1 
