# 재귀는 안되나봐...
R, C = map(int, input().split())
board = [input() for _ in range(R)]
max_v = 0

# 말 옮기는 로직
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
search = {(0, 0, board[0][0])}

while search and max_v < 26:
    i, j, word = search.pop()
    max_v = max(len(word), max_v)
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in word:
            search.add((ni, nj, word + board[ni][nj]))

print(max_v)

# # 시간초과 (1%)
#
# from collections import deque
# R, C = map(int, input().split())
# board = [input() for _ in range(R)]
# cnt = 0
# max_cnt = 0
#
# # 말 옮기는 로직
# di = [0, 1, 0, -1]
# dj = [-1, 0, 1, 0]
# lst = deque()
#
# def dfs(i, j, cnt):
#     global max_cnt
#     lst.append(board[i][j])
#     cnt += 1
#     for k in range(4):
#         ni, nj = i + di[k], j + dj[k]
#         if 0 <= ni < R and 0 <= nj < C:
#             if board[ni][nj] not in lst:
#                 dfs(ni, nj, cnt)
#
#     lst.pop()
#     max_cnt = max(cnt, max_cnt)
#
# dfs(0, 0, cnt)
# print(max_cnt)

# 시간초과 2 (64%)
# R, C = map(int, input().split())
# board = [input() for _ in range(R)]
# cnt = 0
# max_cnt = 0
#
# # 말 옮기는 로직
# di = [0, 1, 0, -1]
# dj = [-1, 0, 1, 0]
# lst = set()
# def dfs(i, j, cnt):
#     global max_cnt
#     lst.add(board[i][j])
#     cnt += 1
#     for k in range(4):
#         ni, nj = i + di[k], j + dj[k]
#         if 0 <= ni < R and 0 <= nj < C:
#             if board[ni][nj] not in lst:
#                 dfs(ni, nj, cnt)
#                 lst.remove(board[ni][nj])
#     max_cnt = max(cnt, max_cnt)
#
# dfs(0, 0, cnt)
# print(max_cnt)