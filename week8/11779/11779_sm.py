import sys, heapq
input = sys.stdin.readline

# 문제
# n(1≤n≤1,000)개의 도시가 있다.
# 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라.
# 항상 시작점에서 도착점으로의 경로가 존재한다.


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

# 가까운 노드 기록쓰
nearnest = [start] * (n + 1)
distance = [1e9] * (n + 1)

q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue

    for next, nextDist in graph[now]:
        cost = nextDist + dist
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now
            heapq.heappush(q, (cost, next))

ans = []
tmp = end
while tmp != start:
    ans.append(str(tmp))
    tmp = nearnest[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))