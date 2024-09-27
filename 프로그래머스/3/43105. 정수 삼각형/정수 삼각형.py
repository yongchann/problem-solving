def solution(triangle):
    level = len(triangle)
    dp = [[0] * i for i in range(1, level+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, level):
        for j in range(i+1):
            if j == 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]
            elif j == i:
                dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
    return max(dp[-1])
    