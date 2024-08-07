from sys import stdin

input = stdin.readline

N, K = map(int, input().split())
loadings = list(tuple(map(int, input().split())) for _ in range(N))
dp = [[0] * (K+1) for _ in range(N+1)]

# dp의 행은 각 물건을 담냐 안 담냐 선택할 것임
# dp의 열은 배낭 무게가 0~K까지일 때의 상황을 가정
# dp에는 가치의 최댓값을 저장할 것임

for i in range(1, N+1):
    for bag_w in range(1, K+1):
        cur_loading = loadings[i-1]
        # 현재 짐(i-1) 무게가 현재 배낭 총 무게보다 무거울 때
        if cur_loading[0] > bag_w:
            # 그냥 이전 짐 선택 시 배낭이 같은 무게일 때의 최댓값
            dp[i][bag_w] = dp[i-1][bag_w]

        else:
            # 해당 짐을 선택하는 것과 선택하지 않는 것 중 최댓값
            # 선택하려면 여유 공간이 있어야 함
            # 선택 x: dp[i-1][bag_w]
            # 선택 o:
            # 1) 현재 짐 가치 +
            # 2) (총 배낭 무게 - 현재 짐 무게)의 배낭에서 v값

            v1 = dp[i-1][bag_w]
            v2 = cur_loading[1]  # 1)
            v2 += dp[i-1][bag_w - cur_loading[0]]  # 2)
            dp[i][bag_w] = max(v1, v2)

print(dp[N][K])

# 실패 과정
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