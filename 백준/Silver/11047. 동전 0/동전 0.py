N, K = map(int, input().split()) 
coins = list()
for i in range(N):
    coins.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coins[i]
    K = K%coins[i] 

print(count)