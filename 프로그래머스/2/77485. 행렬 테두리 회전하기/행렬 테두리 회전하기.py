def get_target_coordinate(x1, y1, x2, y2):
    s = []
    for y in range(y1, y2):
        s.append([x1, y])
    for x in range(x1, x2):
        s.append([x, y2])
    for y in range(y2, y1, -1):
        s.append([x2, y])
    for x in range(x2, x1, -1):
        s.append([x, y1])
    return s
        

def solution(rows, columns, queries):
    answer = []
    nums = list(range(1, rows*columns+1))
    graph = [nums[i:i+columns] for i in range(0, len(nums), columns)]
    
    for query in queries:
        x1, y1, x2, y2 = list(map(lambda x : x-1, query))
        target = get_target_coordinate(x1, y1, x2, y2)        
        
        # 최솟값 획득
        target_value = [graph[xy[0]][xy[1]] for xy in target]
        answer.append(min(target_value))
        
        # 회전
        rotated_value = [target_value[-1]] + target_value[:-1]
        for i in range(len(target)):
            x, y = target[i]
            graph[x][y] = rotated_value[i]

    return answer