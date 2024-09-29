from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    conn = list(map(int, input().split()[:-1]))
    start = conn[0]
    for i in range(1, len(conn)-1, 2):
        neighbor, dist = conn[i], conn[i+1]
        tree[start].append((neighbor, dist))

def bfs(tree, start):
    distances = [-1] * len(tree)
    distances[start] = 0
    q = deque([start])

    furthest_node, max_dist = None, 0
    while q:
        node = q.popleft()
        for neighbor, dist in tree[node]:
            if distances[neighbor] == -1: # 첫 방문 노드
                distances[neighbor] = distances[node] + dist
                q.append(neighbor)
                if distances[neighbor] > max_dist:
                    max_dist = distances[neighbor]
                    furthest_node = neighbor

    return furthest_node, max_dist

furthest_node, _ = bfs(tree, 1)
_, diameter = bfs(tree, furthest_node)
print(diameter)