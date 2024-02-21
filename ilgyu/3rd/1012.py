import sys
sys.stdin = open('input.txt')
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
def need_worm(i, j):
    q = deque()
    start = [i, j]
    q.append(start)

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        if cabbage[x][y] == 1:
            for k in range(4):
                nx, ny = x + di[k], y + dj[k]
                if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                    if cabbage[nx][ny] == 1:
                        visited[nx][ny] = True
                        q.append([nx, ny])




T = int(input())
for tc in range(1, T+1):
    M, N, K =  map(int, input().split()) # 가로 / 세로 / 배추심어진 위치의 개수
    cabbage = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        # print([y,x])
        cabbage[row][col] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == False:
                need_worm(i,j)
                cnt += 1

    print(cnt)
