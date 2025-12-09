import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 시작 정점의 번호
k = int(input())

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] * (n+1) for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    print(f"시작 노드: {start}")
    print(f"초기 거리 배열: {distance[1:]}")
    
    while q:
        print(f"\n현재 힙 상태: {q}")
        dist, now = heapq.heappop(q)
        print(f"힙에서 꺼낸 노드: {now} (현재 거리: {dist})")
        print(f"현재 거리 배열: {distance[1:]}")
        
        if distance[now] < dist:
            print(f"  이미 처리된 노드 {now} (기존 거리 {distance[now]} < {dist}) → 스킵")
            continue
        
        for i in graph[now]:
            next_node = i[0]
            next_cost = i[1]
            cost = dist + next_cost
            print(f"  {now} → {next_node} (간선 비용: {next_cost}, 누적 비용: {cost})")
            
            if cost < distance[next_node]:
                print(f"    거리 갱신: {next_node}번 노드의 기존 거리 {distance[next_node]} → {cost}")
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
                print(f"    힙에 추가: ({cost}, {next_node})")
            else:
                print(f"    기존 거리 {distance[next_node]}가 더 짧음 → 스킵")

# 다익스트라 알고리즘을 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])