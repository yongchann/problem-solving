from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    
    # cmp_to_key
    #    positive return means switching
    #    negative return means non-switching
    numbers.sort(key=cmp_to_key(lambda x, y : -1 if int(x+y) > int(y+x) else 1))
    
    return str(int("".join(numbers)))

