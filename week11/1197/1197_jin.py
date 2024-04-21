# 그래프 - 최소 비용 문제
# 1) 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리 -> MST
# 2) 두 정점 사이의 최소 비용의 경로 찾기 -> 다익스트라

# 신장트리
# 모든 정점을 연결
# 사이클 x, 부분 그래프 == 간선의 개수: n-1
# 한 그래프에서 여러개 나올 수 있음 -> 하나 찾고 끝내면 안된다!

# 최소 신장트리
# 신장트리 중, 간선들의 가중치의 합이 최소인 것

# 예시 문제,
# N개의 도시를 연결하는 도로를 건설하려 할 때,
# 모든 도시에 갈 수 있도록
# 가장 비용이 적게 들도록
# 도로를 건설

# 방법1) 한 정점에서 출발해서, 내가 갈 수 있는 곳들 중 제일 짧은 곳으로!
# 그리디의 일종
# 모든 정점을 방문할 때까지
# bfs랑 어느 정도 유사
# 우선순위 큐를 활용
# => Prim 알고리즘

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

from heapq import heappop, heappush


def prim(start):
    pq = []
    # MST에 포함되었는지 여부
    visited = [0] * V

    # init
    heappush(pq, (0, start))  # weight, start

    while pq:
        weight, v = heappop(pq)

        if visited[v]:  # 방문한 적 있으면
            continue

        visited[v] = 1  # 없는 경우, 방문!



V, E = map(int, input().split())
# 인접행렬 방식
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w

# 방법2) 전체 간선들 중에 제일 가중치가 적은 곳부터 선택!
# 간선 정보를 정렬해야 함

