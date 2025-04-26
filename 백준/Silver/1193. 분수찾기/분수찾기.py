""" 
1 1/1 
2 1/2
3 2/1
4 3/1
5 2/2
6 1/3
9 = 1+2+3+(1,2,3,4)
14 = 1+2+3+4+ (5,4,3,2) (1,2,3,4,5)
"""
n = int(input()) # n =14
sum = 1
cnt = 1
while sum<n: # (sum,cnt)
  cnt += 1
  sum += cnt
 
# cnt = 5
# 1~4까지의 합 = s, n - s = 4칸
# a / b
# cnt-(4-1)칸 / 1 + (4-1)칸
# cnt가 짝수 a가 1부터, cnt 홀수 a가 cnt부터
s = 0
for i in range(cnt):
  s += i
num = n - s - 1
if(cnt % 2 == 0):
  print("%d/%d" %(1+(num),cnt-(num)))
else:
  print("%d/%d" %(cnt-(num),1+(num)))

