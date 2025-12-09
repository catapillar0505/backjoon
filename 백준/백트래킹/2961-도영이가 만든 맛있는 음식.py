#목표: 모든 부분집합에 대해 신맛 곱과 쓴맛 합의 차이 최소화
#방법: 현재까지 선택한 재료들의 곱/합 값만 유지하면 됨
#반복횟수: 5

import sys
input = sys.stdin.readline

n = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

def dfs(idx, sour, bitter, used):
    global min_diff
    if idx == n:
        if used:  # 최소 1개 이상 사용했을 때만
            min_diff = min(min_diff, abs(sour - bitter))
        return
    
    # 현재 재료 사용
    s, b = ingredients[idx]
    dfs(idx+1, sour*s, bitter+b, True)
    
    # 현재 재료 미사용
    dfs(idx+1, sour, bitter, used)

dfs(0, 1, 0, False)
print(min_diff)