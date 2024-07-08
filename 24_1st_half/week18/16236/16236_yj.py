from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

INF = int(1e9)
c_x, c_y = 0, 0
size = 2
eat = 0
time = 0

# 아기 상어 위치
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            c_x, c_y = i, j
            arr[i][j] = 0

def bfs():
    q = deque([(c_x, c_y)])
    visited = [[0] * N for _ in range(N)]
    visited[c_x][c_y] = 0
    fish = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if arr[nx][ny] <= size:  # 지나갈 수 있는 곳
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if 1 <= arr[nx][ny] < size: # 먹을 수 있는 물고기
                        fish.append((visited[nx][ny], nx, ny))

    if not fish:
        return False
    fish.sort()
    return fish[0]  # 가장 가까운 물고기

while True:
    ans = bfs()
    if not ans:  # 먹을 수 있는 물고기 없는 경우
        break

    time += ans[0]
    nx = ans[1]
    ny = ans[2]
    arr[nx][ny] = 0
    c_x, c_y = nx, ny
    eat += 1

    if size == eat:
        size += 1
        eat = 0

print(time)