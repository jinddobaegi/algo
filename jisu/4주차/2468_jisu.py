from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 최댓값 갱신하는 코드
max_v = 0
for i in range(N):
    max_v = max(max_v, max(arr[i]))

# bfs 코드
def bfs(i, j, a):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > a and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1

# 문제 구현
max_cnt = 0
for a in range(max_v):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > a and not visited[i][j]:
                bfs(i, j, a)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)


# import sys
# sys.setrecursionlimit(100000)
# # dfs 코드 (메모리 초과, 재귀 절대 안되는듯)
# def dfs(i, j, a):
#     if i == N - 1 and j == N - 1:
#         # print('리턴')
#         return
#
#     visited[i][j] = 1
#     for k in range(4):
#         ni, nj = i + di[k], j + dj[k]
#         if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] > a:
#             visited[ni][nj] = 1
#             dfs(ni, nj, a)

# 최적화 실패...
# # 최댓값 갱신하는 코드
# max_v = 0
# min_v = 101
# for i in range(N):
#     max_v = max(max_v, max(arr[i]))
#     min_v = min(min_v, min(arr[i]))
#
# # 문제 구현
# max_cnt = 0
# for a in range(min_v, max_v):
#     if min_v == max_v: # 최대 최소가 같으면 무조건 1 아님?
#         print(1)
#         break
#
#     visited = [[0] * N for _ in range(N)]
#     cnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] > a and not visited[i][j]:
#                 bfs(i, j, a)
#                 cnt += 1
#     max_cnt = max(max_cnt, cnt)
# print(max_cnt)