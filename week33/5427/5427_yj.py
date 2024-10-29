# 틀렸습니다 뜨는데 왜 틀렸는지 도저히 모르겠음 ..
from collections import deque

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())  # 빌딩 지도의 너비와 높이
    arr = [list(input().strip()) for _ in range(h)]

    q = deque()
    visited = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                q.append((i, j, 'f'))
                visited[i][j] = 0
            elif arr[i][j] == '@':
                q.append((i, j, 'p'))
                visited[i][j] = 0

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    def bfs():
        while q:
            x, y, t = q.popleft()

            # 빌딩 탈출
            if t == 'p' and (x == 0 or x == h - 1 or y == 0 or y == w - 1):
                return visited[x][y] + 1

            for k in range(4):
                ni = x + di[k]
                nj = y + dj[k]

                if 0 <= ni < h and 0 <= nj < w:
                    if t == 'f' and arr[ni][nj] == '.' and visited[ni][nj] == -1:
                        visited[ni][nj] = visited[x][y] + 1
                        q.append((ni, nj, 'f'))

                    elif t == 'p':
                        if arr[ni][nj] == '.' and (visited[ni][nj] == -1 or visited[ni][nj] > visited[x][y] + 1):
                            visited[ni][nj] = visited[x][y] + 1
                            q.append((ni, nj, 'p'))

        return "IMPOSSIBLE"

    print(bfs())