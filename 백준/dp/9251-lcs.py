import sys
input = sys.stdin.readline

def solve():
    a = input().strip()
    b = input().strip()

    n = (len(a) + 1)
    m = (len(b) + 1)

    dp = [[0] * n for _ in range(m)]

    for i in range(1,n):
        for j in range(1,m):
            if a[i-1] == b[j-1]: # 마지막 문자열 같은 거 확정이니까 +1 /  a,b 문자열 모두 마지막 문자 버리고 그 나머지를 비교한 값 가져오기 => 위치 대각선 위
                dp[i][j] = dp[i-1][j-1] + 1
            else: # 마지막 문자열 다를때 => a의 마지막 문자 버린 버전 vs b의 마지막 문자 버린 버전 비교해서 최댓값으로
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(dp[n-1][m-1]) 

if __name__ == "__main__":
    solve()


