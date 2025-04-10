n = int(input())
dp = [1]*(n+1)

for i in range(2, n+1):
    dp[i] = sum(dp[j]*dp[i-j-1] for j in range(i))

print(dp[n])