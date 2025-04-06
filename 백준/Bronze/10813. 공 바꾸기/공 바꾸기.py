# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
n,m = map(int,input().split())
basket=[i+1 for i in range(n)] # 초기화


#둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
for _ in range(m):
  i,j = map(int,input().split())
  basket[i-1],basket[j-1] = basket[j-1],basket[i-1]
#도현이는 입력으로 주어진 순서대로 공을 교환한다.
#1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
print(*basket)