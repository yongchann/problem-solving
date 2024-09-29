from heapq import heappush, heappop
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

# start 노드로부터의 최단거리 탐색, 우선순위 큐 사용
distances = [float('inf')] * (v+1)
distances[start] = 0
pq = [(0, start)]
while pq:
    distance, node = heappop(pq)
    
    for neighbor, cost in graph[node]:
        if distances[neighbor] > distance + cost:
            distances[neighbor] = distance + cost
            heappush(pq, (distance + cost, neighbor))

for dist in distances[1:]:
    if dist == float('inf'):
        print('INF')
    else:
        print(dist)