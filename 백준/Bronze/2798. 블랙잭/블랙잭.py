# 카드의 개수 N, M에 최대한 가까운 카드 3장의 합
n,m = map(int,input().split())
a = list(map(int,input().split()))
result = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if a[i]+a[j]+a[k]>m:
        continue
      else:
        result = max(result, a[i]+a[j]+a[k])
print(result)