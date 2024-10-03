import heapq

def dijkstra(graph, start, end):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    pq = [(0, start)]
    visited = [False] * len(graph)

    while pq:
        dist, node = heapq.heappop(pq)

        if node == end:
            return dist

        if visited[node]:
            continue

        visited[node] = True

        for cost, neighbor in graph[node]:
            if not visited[neighbor]:
                new_dist = dist + cost
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    # 여기서 큐에 넣는 대신, 거리를 갱신만 합니다.

        # 방문하지 않은 노드 중 가장 가까운 노드를 찾아 큐에 넣습니다.
        next_node = min((i for i in range(len(graph)) if not visited[i]), key=lambda x: distances[x], default=None)
        if next_node is not None:
            heapq.heappush(pq, (distances[next_node], next_node))

    return float('inf')  # 경로가 없는 경우

# 그래프 입력 받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

departure, destination = map(int, input().split())

# 최단 거리 계산
shortest_distance = dijkstra(graph, departure, destination)
print(shortest_distance)