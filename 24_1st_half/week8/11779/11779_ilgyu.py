import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(s, t):
    pq = []
    heapq.heappush(pq, (0, s)) # 누적비용, 현재, 목적도시, 여태까지의 경로
    total_cost[s] = 0
    # 경로를 어떻게 추적하지
    prev_city = [0] * (n + 1)  # 경로기록

    while pq:
        cost, current = heapq.heappop(pq)
        if current == t:
            break

        for next_city, money in graph[current]:
            next_cost = cost + money
            if total_cost[next_city] <= next_cost:
                continue
            total_cost[next_city] = next_cost
            prev_city[next_city] = current # next_city로 이동할거니까 prev(경로기록리스트)에는 next_city인덱스의 값을 current로
            # 이렇게하면 prev[2] = 1 인경우 2번 노드 이전엔 1번노드였따는 뜻
            heapq.heappush(pq, (next_cost, next_city))

    path = [] # 최종 경로
    while t != 0: # 역추적 해가는 과정이니까 t(목적지가 0 이 될 떄까지 while돌리는겨)
        path.append(t) # 맨첨엔 t가 내가 설정한 target_city
        t = prev_city[t] # target_city = prev_city[t] => 그니까 여기선 t의 초기값이 5인데 내가 위에 for문 돌리면서
                         # prev_city[5] = 이전 노드 / 이런식으로 저장을 했으니까 그 값을 찾아서 최종경로인 path에 넣어주기 위해서
                         # 예를들어 prev_city가 위 while문이 다 끝나고
                         # [0, 0, 0, 1, 0, 3] 이런형태가 됐다하면
                         # t = 5인 시점에서
                         # path.append(5) => path = [5]
                         # t = prev_city[5] = 3
                         # t = 3이니까 while조건에 만족해서 또 돌아
                         # path.append(3) => path = [5, 3]
                         # t = prev_city[3] = 1
                         # t = 1
                         # path.append(1) => path = [5, 3, 1]
                         # t = prev_city[1] = 0
                         # 이 시점에선 while 조건문에 걸려서 더이상 안돎 => 경로 완성
    path.reverse()
    return path


n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for _ in range(n+1)]
# print(graph)
for _ in range(m):
    s, e, c = map(int, input().split()) # 출발, 도착, 비용
    graph[s].append([e, c])

start_city, target_city = map(int, input().split())
# print(target_city)

total_cost = [float('inf')] * (n+1)

path = dijkstra(start_city, target_city)
print(total_cost[target_city])
print(len(path))
print(' '.join(map(str, path)))


