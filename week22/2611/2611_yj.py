# 아직 못 풀었습니다^^..
import heapq

N = int(input())
M = int(input())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    p, q, r = map(int, input().split())
    arr[p].append((q, r))

def d(s):
    pq = []
    route = [0 for _ in range(N+1)]
    heapq.heappush(pq, (0, s))

    while pq:
        dist, now = heapq.heappop(pq)

        for next, cost in arr[now]:
            new_dist = dist + cost

    return