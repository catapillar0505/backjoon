# 2차원 좌표 평면 = 2차원 배열
arr = [[0 for _ in range(101)] for _ in range(101)]

n = int(input())

for _ in range (n):
  x,y = map(int,input().split()) # 5 2 - 5,2  6,2 ... 15,2 | 
  for i in range(y,y+10):
    for j in range(x,x+10):
      arr[j][i] = 1

count = 0
for row in arr:
  count += row.count(1)
  
print(count)
