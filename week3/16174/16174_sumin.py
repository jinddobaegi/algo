# 점프왕 젤리 (Large)
# 실버 1

import sys

# 정사각형 구역 내부에서만 움직이기 가능 -> 구역 외로 가면 즉시 패배 Hing
# 출발점 : 왼쪽 위 칸
# 이동방향 : 오른쪽 / 아래
# 가장 아래칸 도달 -> 승리 HaruHaru
# 한번에 이동가능한 칸 수 : 현재 밟는 칸에 쓰인 수

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx, dy = [1,0], [0,1]

def in_range(x,y):
    return 0<=x<N and 0<=y<N
def dfs(x, y):
    # 일단 방문 체크
    visited[x][y] = 1
    for i in range(2):
        nx = x + dx[i] + board[x][y]
        ny = y + dy[i] + board[x][y]
        if in_range(nx, ny) and not visited[nx][ny]:
            if board[nx][ny] == -1:
                print("HaruHaru")
                # return(0)  -> 이거 하니까 틀리네요..
                exit(0)
            else:
                dfs(nx, ny)
    return False
# 아니면 힝입니다
if not dfs(0, 0):
    print("Hing")

