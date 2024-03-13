
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    
    visited[0][0] = True
    q = deque([(0, 0, 1)]) # (y, x, depth)

    while q:
        y, x, d = q.popleft()
        print(y, x, d)
        if y == n-1 and x == m-1:
            return d
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and maps[ny][nx] == 1:
                q.append((ny, nx, d+1))
                visited[ny][nx] = True
                
                
    return -1

