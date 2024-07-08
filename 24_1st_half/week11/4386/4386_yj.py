# 최소 스패닝 트리
import sys
import heapq
from math import sqrt
input = sys.stdin.readline

N = int(input())
stars = []

for _ in range(N):
    x, y = map(float, input().strip().split())
    stars.append((x, y))

# 별들 간의 거리 정보를 인접 리스트로 저장
arr = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)   # 별들 간의 거리 계산
        # 인접 리스트에 거리 정보 추가
        arr[i].append((j, distance))
        arr[j].append((i, distance))

def prim(start):
    heap = []
    MST = [0] * (N+1)

    heapq.heappush(heap, (0, start))
    sum_cnt = 0
    sum_dist = 0

    while heap:
        # N개의 정점을 가지는 그래프에 대해 반드시 N-1개의 간선만 사용해야 함
        if sum_cnt == N:
             break

        dist, star = heapq.heappop(heap)   # 가장 적은 비용을 가진 정점을 꺼냄

        if MST[star]:   # 이미 방문한 노드라면 pass
            continue

        MST[star] = 1   # 방문 체크
        sum_cnt += 1
        sum_dist += dist
        for star, dist in arr[star]:
            heapq.heappush(heap, (dist, star))

    return sum_dist

print(f"{prim(0):.2f}")