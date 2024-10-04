def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n
    
    total_cost = 0
    edges = 0
    
    for cost in costs:
        x, y, weight = cost
        
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
            total_cost += weight
            edges += 1
        
        if edges == n - 1:
            break
    
    return total_cost