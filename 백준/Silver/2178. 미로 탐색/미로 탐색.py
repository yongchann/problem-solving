from collections import deque

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

visited[0][0] = True
q = deque([(1, (0, 0))])

while q:
    distance, pos = q.popleft()
    if pos == (n-1, m-1):
        print(distance)
        break
    
    for i in range(4):
        y = pos[0]+directions[i][0]
        x = pos[1]+directions[i][1]
        
        if 0<=y<n and 0<=x<m and not visited[y][x] and graph[y][x] =='1':
            visited[y][x] = True
            q.append((distance+1, (y,x)))