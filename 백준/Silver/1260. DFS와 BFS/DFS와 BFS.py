from collections import deque
import sys
sys.setrecursionlimit(10000) # 또는 10 ** 6
n, m, v = map(int, input().split())
graph = [set() for _ in range(n+1)]

# 입력
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].add(j)
    graph[j].add(i)
    
for i in range(n+1):
    graph[i] = (sorted(list(graph[i])))

def dfs(node, visited):
    global graph
    if visited[node]:
        return
    
    visited[node] = True
    print(node, end=" ")
    
    for i in graph[node]:
        if not visited[i]:
            dfs(i, visited)
        

def bfs(graph, n, start):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    
    while q:
        node = q.popleft()
        print(node, end=" ")
            
        for i in graph[node]:
            if not visited[i]:
                q.append(i)   
                visited[i] = True
                 

dfs(v, [False] * (n+1))
print()
bfs(graph, n, v)
