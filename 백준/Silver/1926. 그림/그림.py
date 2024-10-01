from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(y, x, visited):
    cnt = 1
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and graph[ny][nx]:
                visited[ny][nx] = True
                cnt += 1
                q.append((ny, nx))
    
    return cnt

answer_cnt = 0
max_area = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            visited[i][j] = True
            answer_cnt += 1
            max_area = max(max_area, bfs(i, j, visited))
            
print(answer_cnt)
print(max_area)