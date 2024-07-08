from collections import deque


# 바이러스 확산 함수
def virus(now_arr):
    visited = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if now_arr[y][x] == 2:
                q = deque()
                visited[y][x] = 1
                q.append((y, x))
                while q:
                    i, j = q.popleft()
                    for num in range(4):
                        ni = i + di[num]
                        nj = j + dj[num]
                        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and now_arr[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                now_arr[i][j] = 2

    return safe_area(now_arr)


# 안전 영역 계산 함수
def safe_area(now_arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if now_arr[i][j] == 0:
                cnt += 1
    return cnt

# 벽을 세우고 안전 영역을 계산하는 함수
def wall(arr, x1, y1, x2, y2, x3, y3):
    now_arr = [row[:] for row in arr]
    now_arr[x1][y1] = 1
    now_arr[x2][y2] = 1
    now_arr[x3][y3] = 1
    ans = virus(now_arr)
    return ans


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lists = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lists.append((i, j))

be_safe = -1
for w1 in range(len(lists)):
    for w2 in range(w1 + 1, len(lists)):
        for w3 in range(w2 + 1, len(lists)):
            x1, y1 = lists[w1]
            x2, y2 = lists[w2]
            x3, y3 = lists[w3]

            sample_safe = wall(arr, x1, y1, x2, y2, x3, y3)
            if be_safe < sample_safe:
                be_safe = sample_safe

print(be_safe)
