from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
loadings = list(tuple(map(int, input().split())) for _ in range(N))

# 무게는 K만큼 담을 수 있음
# 1) 가치를 우선으로 담아보자 -> 실패
# loadings.sort()
# max_v = 0
# weight = 0
# idx = N-1
# while idx >= 0:
#     w, v = loadings[idx]
#     new_w = weight + v
#     if new_w > K:  # 이번 물건 담았을 때 배낭 넘치면
#         idx -= 1
#         continue
#     weight = new_w
#     max_v += v
#     idx -= 1
#
# print(max_v)

# 2) 백트래킹과 dfs를 활용? -> 시간 초과
# def knapsack(idx, weight, value):
#     global max_v
#
#     if weight > K:
#         return
#
#     max_v = max(max_v, value)
#
#     if idx == N:
#         return
#
#     visited[idx] = 1
#     loading = loadings[idx]
#     knapsack(idx+1, weight+loading[0], value+loading[1])
#     visited[idx] = 0
#     knapsack(idx+1, weight, value)
#
#
# max_v = 0
# visited = [0] * N
# knapsack(0, 0, 0)
# print(max_v)