from collections import deque

def bfs(N, M):
    q = deque([(0, 0, 0)])  # (i, j, 움직인 횟수)
    visited = [[-1] * M for _ in range(N)]
    visited[0][0] = 0
    max_v = 0

    while q:
        i, j, cnt = q.popleft()
        move = int(board[i][j])

        for di, dj in direction:
            ni, nj = i + (di * move), j + (dj * move)

            if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 'H':  # 보드 내부로 이동하면
                if visited[ni][nj] == -1 or visited[ni][nj] < cnt + 1:
                    visited[ni][nj] = cnt + 1
                    q.append((ni, nj, cnt + 1))
                    max_v = max(max_v, cnt + 1)
                elif visited[ni][nj] >= 50 * 50:  # 무한 루프 어케 앎?
                    return -1
    return max_v + 1


N, M = map(int, input().split())  # 세로크기 N, 가로크기 M
board = [input().strip() for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


ans = bfs(N, M)
print(ans)
