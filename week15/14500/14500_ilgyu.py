import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(x, y, count, total):
    global max_value

    if count == 4:
        max_value = max(max_value, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1, total + area[nx][ny])
            visited[nx][ny] = False

def check_extra_shapes(x, y):
    global max_value
    for shape in extra_shapes:
        try:
            total = area[x][y] + area[x + shape[0][0]][y + shape[0][1]] + area[x + shape[1][0]][y + shape[1][1]] + area[x + shape[2][0]][y + shape[2][1]]
            max_value = max(max_value, total)
        except IndexError:
            continue

N, M = map(int, input().split()) #세로 가로
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

extra_shapes = [
    [(0, 1), (0, 2), (-1, 1)],  # ㅗ
    [(0, 1), (0, 2), (1, 1)],   # ㅜ
    [(1, 0), (2, 0), (1, 1)],   # ㅏ
    [(1, 0), (2, 0), (1, -1)]   # ㅓ
]

max_value = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, area[i][j])
        visited[i][j] = False
        check_extra_shapes(i, j)

print(max_value)