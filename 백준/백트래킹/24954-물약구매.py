# 📌 문제 목표
# N개 물약을 모두 구매하는 최소 비용 (특정 물약 구매 시 다른 물약 할인)
# 💡 해법 요약

# 메모이제이션 DFS로 모든 구매 순서 탐색
# 구매한 물약 집합과 현재 가격을 상태로 저장
# 각 상태에서 안 산 물약들 시도하며 최소값 갱신
#반복횟수: 1
import sys
from functools import lru_cache
input = sys.stdin.readline

# 입력
n=int(input()) # 물약개수
cost = list(map(int, input().split())) # 가격
sale = [[] for _ in range(n)]

for i in range(n): # 각 물약에 대한
    m=int(input())  # 할인 정보 개수
    for _ in range(m):
        x,d = map(int, input().split()) # 3 10
        sale[i].append((x-1, d)) # 인덱스라 x-1을 해줌

@lru_cache(maxsize=None)
def dfs(purchased,current_prices):
    # 종료조건
    if len(purchased) == n: # 모든 물약을 다 샀나?
        return 0
    #모든경우시도해보기
    min_val = float('inf') # 일단 엄청 큰 수로 시작
    prices = list(current_prices) # 현재 가격표 복사


    for i in range(n): # 각 물약을 확인
        if i not in purchased: # 아직 안 산 물약이면
            price = prices[i] # # i번 물약의 현재 가격
            # 할인 적용
            new_prices = prices[:] # 가격표 복사
            for k, d in sale[i]: # i번 물약을 사면 생기는 할인들
                new_prices[k] = max(1,new_prices[k]) # 할인! (최소 1원)
            
            # 재귀 호출
            new_purchased = tuple(sorted(list(purchased) + [i])) # 구매 목록에 추가
            result = price + dfs(new_purchased, tuple(new_prices))
            min_val = min(min_val, result) # 가장 싼 방법 기억
    
    return min_val

print(dfs((), tuple(cost)))