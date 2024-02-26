# 유기농 배추
# 실버 2

import sys
# setrecursionlimit : 재귀의 깊이를 설정/제한 (기본은 1000까지만 됨)
sys.setrecursionlimit(2500)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    # 함수 한 번 실행될 때마다 해당 구역을 방문 처리
    visited[x][y] = 1

    # 상하좌우를 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나면 계산을 하지 않겠다 히힣
        if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
        # 방문을 한 곳이라면 더이상 안하겠다 히힣
        if visited[nx][ny] == True: continue

        # 만약 nx, ny 가 1이라면 다음 dfs탐색
        if board[nx][ny] == 1: dfs(nx, ny)


T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    # 지나간 경로 체크
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        # 해당 좌표에 있는 것들은 다 board에 1을 써주기
        board[x][y] = 1

    # row col을 잘 살펴야하므로 range를 N으로 할지 M으로 할지 잘 보고 해야함
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and board[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)




