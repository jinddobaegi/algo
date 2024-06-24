# 특정한 경로
# 골드 4

'''
방향성 없는 그래프 -> 간선 정보 저장할 떄, 양쪽 노드에 다 해주는 거 잊지말긔
1번 -> N번으로 최단거리 이동할 예정

임의의로 주어진 두 정점은 꼭 통과하기!!

-> 다익스트라 알고리즘으로 최단거리 구하기
'''

import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
edges = [[] for i in range(n+1)]

# 양쪽 노드 정보 저장
for i in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

ans = float('inf')


def dijkstra(start, s):
    # 시작노드로부터 모든 노드까지 최단거리 저장할 리스트 무한대로 초기화
    distance = [ans] * (n+1) # 이거 몰랐는데 블로그 참고함

    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0 # 시작 노드 최단거리 0으로

    # 큐 빌떄까지
    while q:
        # 가장 짧은 거리 노드 꺼내
        dist, node = heapq.heappop(q)

        # 현재 노드 최단 거리가 이미 계산된 거리보다 작으면 무시ㄱ
        if distance[node] < dist:
            continue

        # 현재 노드 인접노드 확인
        for next, w in edges[node]:
            # 인접 노드 거쳐가는 새로운 거리 계산해주기
            cost = dist + w

            # 새로운 거리가 기존 거리보다 짧으면 갱신
            # 우선순위 큐에 추가
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q, [cost, next])

    return distance

# 최단 경로 담아
d1 = dijkstra(1, n)
d2 = dijkstra(v1, n)
d3 = dijkstra(v2, n)


# v1을 먼저 들리거나
# v2를 먼저 들리거나
# 둘 중 더 짧은 거리 쓰자
result = min(d1[v2] + d2[n] + d3[v1], d1[v1] + d2[v2] + d3[n])


if result == ans:
    print(-1)
else:
    print(result)











# 이거 하다가 포기
# def dijkstra(start, end):
#     # 최단거리 저장 리스트
#     short = [ans] * (n+1)
#     # 시작 노드 최단 거리
#     short[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#
#     # 우선순위 큐 비어있지 않은 동안 반복
#     while q:
#         # 가장 짧은거리 노드 꺼내기
#         dis, node = heapq.heappop(q)
#
#         # 이미 처리된거보다 큐에서 꺼낸 거리가 더 크면 무시 ㄱ
#         if short[node] < dis:
#             continue
#
#     # 현재 노드랑 인접 노드 확인
#     for ad_node, ad_dis in edges[node]:
#         new_dis = short[node] + ad_dis
#

