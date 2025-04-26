# 첫째 줄에 N이 주어진다
n = int(input())
sum = 1
cnt = 1
while(sum<n):
  sum += 6*cnt
  cnt += 1
print(cnt)