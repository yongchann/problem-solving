from collections import deque

def solution(board):
    # 초기화
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    row, col = len(board), len(board[0])
    visited = [[False] * col for _ in range(row)]
    
    start, goal, obstacles = [], [], set()
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                start = [i, j]
            elif board[i][j] == 'G':
                goal = [i, j]
            elif board[i][j] == 'D':
                obstacles.add((i, j))

    def move(y, x, i):
        while 0<=y<row and 0<=x<col and (y,x) not in obstacles:
            y += dy[i]
            x += dx[i]
        return y-dy[i], x-dx[i]
                
    # BFS
    y, x = start
    visited[y][x] = True
    q = deque([[y, x, 0]])
    while q:
        y, x, distance = q.popleft()
        if [y, x] == goal: return distance
        
        for i in range(4):
            _y, _x = move(y, x, i)
            if not visited[_y][_x]:
                visited[_y][_x] = True
                q.append([_y, _x, distance+1])
    
    return -1