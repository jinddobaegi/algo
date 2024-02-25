# 유기농 배추

import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global visited
    visited[y][x] = True
    for num in range(4):
        nx, ny = x + dx[num], y + dy[num]
        if nx < 0 or M <= nx or ny < 0 or N <= ny: # 벗어나면 걸러
            continue
        if field[ny][nx] and not visited[ny][nx]:
            dfs(nx, ny)

T = int(input())

for tc in range(T):
    # 가로길이 M, 세로길이 N, 배추 개수 K
    M, N, K = map(int, input().split())
    cabbage = [list(map(int, input().split())) for _ in range(K)]
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for i in range(K): # field 채우기
        # [X, Y] == [1, 0]
        x, y = cabbage[i]
        field[y][x] = 1

    cnt = 0
    for x in range(M):
        for y in range(N):
            if field[y][x] and not visited[y][x]: # 지금 방문한 지점이 첫 방문지라면?
                dfs(x, y) # 거기서 상하좌우로 있는애들 다 연결해서 방문자목록에 넣어버려
                cnt += 1
    print(cnt)
