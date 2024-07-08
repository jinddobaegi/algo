# 외판원 순회
# 시간초과 ㅠ
import sys

# def move(N, cost):
#     def dfs(now, visited, total):
#         min_cost = sys.maxsize
#         if len(visited) == N:
#             if cost[now][0] > 0:
#                 return total + cost[now][0]
#
#         for next in range(N):
#             if next not in visited and cost[now][next] > 0:
#                 visited.add(next)
#                 min_cost = min(min_cost, dfs(next, visited, total + cost[now][next]))
#                 visited.remove(next)
#
#         return min_cost
#
#     # 시작 도시는 0번 도시로 고정
#     start = 0
#     visited = set([start])
#     return dfs(start, visited, 0)


N = int(input()) # 도시의 수
cost = [list(map(int, input().split())) for _ in range(N)]
ans = move(N, cost)

print(ans)