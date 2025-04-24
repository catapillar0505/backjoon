# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) 예 ) ZZAZZ 36
N, B = input().split()
B = int(B)
# 진법 변환의 숫자 체계 : A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
number_system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 첫째 줄에 B진법 수 N을 10진법으로 출력한다. 예) 60466175
res = 0
# 전체 리스트 거꾸로 뒤집기
N = N[::-1]

for i,n in enumerate(N):
  res += number_system.index(n) * (B ** i) # z * 36의 0승
print(res)   