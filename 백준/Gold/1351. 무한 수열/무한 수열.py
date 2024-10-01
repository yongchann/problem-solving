import sys
sys.setrecursionlimit(10**6)

n, p, q = map(int, input().split())
d = {0:1}

def find(i):
    if i in d:
        return d[i]
    
    d[i//p] = find(i//p)
    d[i//q] = find(i//q)
    return find(i//p) + find(i//q)

print(find(n) if n != 0 else 1)