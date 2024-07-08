from collections import deque

di = [0, 1]
dj = [1, 0]

def game_start(i, j):
    q = deque()
    start = [i, j]
    q.append(start)
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        visited[x][y] = True
        d = area[x][y]
        if d == -1:
            print("HaruHaru")
            return
        for k in range(2):
            nx, ny = x + d * di[k], y + d * dj[k] # 0 + 1 * 0 / 0 + 1 * 1
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if area[nx][ny] == -1:
                    print("HaruHaru")
                    return
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = True

    print("Hing")


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
# print(area)
visited = [[False] * n for _ in range(n)]
game_start(0, 0)