import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque()

# 일단 익은 토마토 찾기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

# 익은 토마토 기준으로 탐색
def bfs():
    while q:
        z, x, y = q.popleft()

        # 방향 다 돌면서 익지 않은 토마토 있으면 익은 토마토 만들기
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1 # 이전 값에 1 더하면서 일수 계산
                q.append((nz, nx, ny))

bfs()

max_d = 0
temp = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                temp = False
            max_d = max(max_d, arr[i][j][k])

if temp == False:
    ans = -1
else:
    ans = max_d - 1

print(ans)


# 틀림
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if arr[i][j][k] == 0:
#                 temp = False
# 
# if temp == False:
#     ans = -1
# else:
#     ans = max(max(map(max, arr)))-1