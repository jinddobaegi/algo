# 점프왕쩰리(Large)

from collections import deque

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        di, dj = q.popleft()
        if [di, dj] == (N - 1, N - 1):
            return
        value = arr[di][dj]
        # 현재 좌표에서 가야되는 거리가 도착점을 넘어선다면 continue
        ni, nj, ai, aj = di + value, dj, di, dj + value
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            q.append([ni, nj])
            visited[ni][nj] = 1
        if 0 <= ai < N and 0 <= aj < N and not visited[ai][aj]:
            q.append([ai, aj])
            visited[ai][aj] = 1

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
bfs()
if visited[N - 1][N - 1]:
    print('HaruHaru')
else:
    print('Hing')