def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for j, i in puddles:
        dp[i][j] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1:
                continue
            if (temp := dp[i-1][j]) != -1:
                dp[i][j] += temp
            if (temp := dp[i][j-1]) != -1:
                dp[i][j] += temp
            
    return dp[-1][-1]%1_000_000_007