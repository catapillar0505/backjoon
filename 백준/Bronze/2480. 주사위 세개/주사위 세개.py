# 입력 조건
a, b, c = map(int, input().split())
prize = 0

if a== b == c:
  prize = 10000 + a * 1000
elif a == b or b == c or a == c:
  if a == b or a == c: prize = 1000 + a * 100
  elif b == c: prize = 1000 + b * 100
else:
  prize = max(a, b, c) * 100
print(prize)