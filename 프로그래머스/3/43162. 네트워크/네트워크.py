from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        # 미방문 노드는 신규 네트워크를 의미합니다.
        if not visited[i]:
            answer += 1
            
            # 해당 노드에 대해 BFS 탐색
            q = deque([i])
            while q:
                node = q.popleft()
                target = [idx for idx, is_connected in enumerate(computers[node]) if not visited[idx] and is_connected]
                for t in target:
                    visited[t] = True
                    q.append(t)
                
    return answer

