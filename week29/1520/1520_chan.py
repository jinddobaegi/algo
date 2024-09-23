import sys
sys.stdin = open("week29/1520/1520.txt") 
from collections import deque
#왼쪽상단에서 오른쪽 하단까지 가는 경로 몇개 인지 구하기 아래로만 내려갈 수 있음

# M, N = map(int, input().split())

# board = [list(map(int, input().split()))for _ in range(M)]

# start = (0, 0)

# def bfs(start):
#     queue = deque([start])
#     # print(queue)
#     visited = [[False]*N for _ in range(M)]
#     count = 0
#     while queue:
#         delta = [(1,0),(-1,0),(0,1),(0,-1)]
#         r, c = queue.popleft()
#         print(r, c)
#         if r == M-1 and c == N-1:
#              count += 1
#         for a, b in delta:
#             nr, nc = r + a, c + b
#             if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc]:
#                 if board[r][c] > board[nr][nc]:
#                     # print(nr, nc)
#                     visited[nr][nc] = True
#                     queue.append((nr, nc))
#     return count

# result = bfs(start)

# print(result)

M, N = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
for i in dp:
    print(i)
print()

for i in board:
    print(i)


delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(r, c):

    if r == M-1 and c == N-1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    
    for a, b in delta:
        nr, nc = a + r, b + c
        if 0 <= nr < M and 0 <= nc < N:
            if board[r][c] > board[nr][nc]:
                dp[r][c] += dfs(nr, nc)
                
    return dp[r][c]

result = dfs(0, 0)
print(result)


