# 바구니 N, 공 넣는 횟수M
n,m = map(int,input().split())
baskect = [0]*n

# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다. 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
for _ in range(m):
  i,j,k = map(int,input().split())
  baskect[i-1:j] = [k]*(j-i+1)
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.
print(*baskect)