# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) 예 60466175 36
n, b = map(int, input().split())
# 진법 변환의 숫자 체계 : A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
number_system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = ""
i = 0
while n:
  x = n%b # 36의 i제곱 * x = n 따라서 x는 n을 36으로 나눈 나머지이다
  if 0<= x <= 9:
    res += str(x)
  else: # A~Z
    res += number_system[x]
  i += 1 # while문 인덱스 증가
  n = n // b # 매 인덱스마다 n을 36으로 나누기(i=0일때는 0번 나눈상태, i=1일때는 1번 나눈상태, i=2일때 2번 나눈상태)

# 리스트 뒤집기
res = res[::-1]

# 첫째 줄에 10진법 수 N을 B진법으로 출력한다 예) ZZZZZ
print(res)