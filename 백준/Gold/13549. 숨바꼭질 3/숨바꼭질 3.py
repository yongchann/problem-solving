from heapq import heappush, heappop

def solve(start, target):
    if start >= target:
        return start - target
    
    MAX = 100001
    visited = [False] * MAX
    pq = [(0, start)]

    while pq:
        sec, pos = heappop(pq)
        if pos == target:
            return sec

        if pos*2 < MAX and not visited[pos*2]:
            visited[pos*2] = True
            heappush(pq, (sec, pos*2))  
        
        if pos > 0 and not visited[pos-1]:
            visited[pos-1] = True
            heappush(pq, (sec+1, pos-1))

        if pos+1 < MAX and not visited[pos+1]:
            visited[pos+1] = True
            heappush(pq, (sec+1, pos+1))

start, target = map(int, input().split())        
print(solve(start, target))