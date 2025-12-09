import sys
import heapq 

input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
graph = [[] for _ in range(n+1)] # 1번 도시부터 시작

for _ in range(m):
    a, b, cost = map(int, input().split()) # a에서 b로 가는 비용이 cost인 버스 노선
    graph[a].append([b, cost])
    print(f"  {a}번 도시 → {b}번 도시 (비용: {cost})")


start, end = map(int, input().split()) # 출발도시와 도착도시

costs = [1e9 for _ in range(n+1)] # 각 도시까지의 최소 비용을 저장 (초기값: 무한대)
heap = []
costs[start] = 0
heapq.heappush(heap, [0, start]) # 힙에 [비용, 도시] 형태로 넣음


while heap:
    print(f"힙: {heap}")
    cur_cost, cur_v = heapq.heappop(heap) # 현재까지 비용이 가장 적은 도시를 꺼냄
    print(f"\n힙에서 꺼낸 도시: {cur_v} (현재 비용: {cur_cost})")
    print(f"현재 비용 배열: {costs[1:]}")
    if costs[cur_v] < cur_cost: # 이미 더 짧은 경로로 방문한 적이 있다면 무시
        print(f"  이미 더 짧은 경로로 방문됨 → 스킵")
        continue
    for next_v, next_cost in graph[cur_v]: # 현재 도시에서 갈 수 있는 다음 도시들을 확인
        sum_cost = cur_cost + next_cost
        print(f"  {cur_v} → {next_v} (추가 비용: {next_cost}, 총 비용: {sum_cost})")
        
        if sum_cost >= costs[next_v]: # 현재까지의 비용 + 다음 도시까지의 비용이 기존보다 크면 무시
            print(f"    기존 비용 {costs[next_v]}보다 크거나 같음 → 스킵")
            continue
        # 더 짧은 경로를 찾았으면 갱신하고, 힙에 추가
        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])
        print(f"    비용 갱신: {next_v}번 도시의 비용 → {sum_cost}")
        print(f"    힙에 추가: {[sum_cost, next_v]}")


print(f"\n최종 비용 배열: {costs[1:]}")
print(f"{start}번 도시에서 {end}번 도시까지의 최소 비용: {int(costs[end])}")
print(costs[end])
print(f"그래프: {graph}")

