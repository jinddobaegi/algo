from sys import stdin, setrecursionlimit
from heapq import heappush, heappop

input = stdin.readline
setrecursionlimit(10**6)

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    adj_list[p].append((q, r))

# dp적 사고를 해보자
# 사이클이 안 생김(예제만 그런 건가..?)
# 특정 노드까지 도달하는 최댓값을 저장


def my_func(s):
    dp = [[0, []] for _ in range(N+1)]
    dp[s][1] = [s]
    pq = []
    heappush(pq, (0, s))  # 거리, 노드 순

    while pq:
        dist, v = heappop(pq)
        # 이전에 더 큰 점수를 얻은 적 있는지?
        if dp[v][0] > dist:
            continue

        route_before = dp[v][1]  # 이전 경로
        for w, cost in adj_list[v]:
            new_dist = dist + cost

            if dp[w][0] >= new_dist:
                continue

            dp[w][0] = new_dist
            dp[w][1] = route_before + [w]  # 현재 경로

            if w != 1:  # 1이면 또 돌 필요 없음
                heappush(pq, (new_dist, w))

    return dp[1]


res = my_func(1)
print(res[0])
print(*res[1])


# def dfs(v, visited, route, score):
#     global max_score, res
#
#     # Init
#     if v == 1 and visited[v] == -1:
#         visited[v] += 1
#         route = [1]
#
#     # 종료 조건
#     if v == 1 and visited[v] == 1:
#         # print('1 두 번째 방문')
#         max_score = max(score, max_score)
#         res = route
#         return
#
#     # 진행
#     for w, r in adj_list[v]:
#         if visited[w] <= 0:  # line 28 참고
#             # print(f'{v}에서 {w}로!')
#             visited[w] += 1  # 1은 두 번 가능
#             dfs(w, visited, route + [w], score + r)
#             visited[w] -= 1


# 1번 노드로 돌아오는 것을 고려하여 1번 인덱스 -1로 설정
# visited = [0] * (N+1)
# visited[1] = -1
# max_score = 0
# res = []
# dfs(1, visited, [], 0)
#
# print(max_score)
# print(*res)