def solution(m, n, puddles):
    mp = [[-1] * m for _ in range(n)]
    
    for i in range(m):
        mp[0][i] = 1
        
    for i in range(n):
        mp[i][0] = 1
        
    for i, j in puddles:
        mp[j-1][i-1] = 0
        if i == 1:
            for k in range(j, n):
                mp[k][0] = 0
        elif j == 1:
            for k in range(i, m):
                mp[0][k] = 0
        
    for i in range(1, n):
        for j in range(1, m):
            if mp[i][j] == 0:
                continue
            mp[i][j] = mp[i-1][j] + mp[i][j-1]
        
    return mp[-1][-1] % 1000000007
            
