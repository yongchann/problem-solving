def solution(data):
    data.sort()
    for i in range(len(data)-1):
        if data[i+1].startswith(data[i]):
            return False
    return True