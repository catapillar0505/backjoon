n,k = map(int,input().split())
items=[tuple(map(int,input().split())) for _ in range(n)]

dp = [[k+1] * [0] for _ in range(n+1)]

for i in range(1,n+1):
    weight, value = items[i] # 현재 물건의 무게와 가치
    for w in range(1,k+1):
        if weight <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
        else:
            dp[i][w] = dp[i-1][w] 
print(dp[n][k])