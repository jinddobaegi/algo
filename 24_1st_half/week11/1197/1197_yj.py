# 최소 스패닝 트리
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 모든 정점들을 가장 적은 수의 간선과 비용으로 연결하는 것
# n개의 정점을 가지는 그래프에 대해 반드시 (n-1)개의 간선만을 사용해야 함

# Prim 알고리즘
# 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
# 임의 정점 하나 선택하고 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점을 선택

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())  # 정점의 개수, 간선의 개수
arr = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())  # A 정점, B 정점, 가중치 C

    arr[A].append([B, C])
    arr[B].append([A, C])

def prim(start):
    heap = []
    # MST에 포함되었는지 여부
    MST = [0] * (V+1)

    heapq.heappush(heap, (0, start))
    sum_dot = 0
    sum_weight = 0

    while heap:
        # V개의 정점을 가지는 그래프에 대해 반드시 V-1개의 간선만 사용해야 함
        if sum_dot == V:
             break

        weight, dot = heapq.heappop(heap)   # 가장 적은 가중치를 가진 정점을 꺼냄

        if MST[dot]:   # 이미 방문한 노드라면 pass
            continue

        MST[dot] = 1   # 방문 체크
        sum_dot += 1
        sum_weight += weight
        for dot, weight in arr[dot]:
            heapq.heappush(heap, (weight, dot))

    return sum_weight

print(prim(1))