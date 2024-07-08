from collections import deque

N = int(input())
picture = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt_rgb = 0
cnt_rrb = 0
q = deque()

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(a, b):
    visited[a][b] = 1 # 방문 체크
    q.append((a, b))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            # 범위안에 있고, 글자가 같고, 방문하지 않았으면 방문자 표시
            if 0 <= ni < N and 0 <= nj < N and picture[i][j] == picture[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))

for i in range(N): # not 적록색약
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_rgb += 1

for i in range(N): # 색약버전으로 picture 바꾸고
    picture[i] = picture[i].replace('G', 'R')


visited = [[0] * N for _ in range(N)]
for i in range(N): # 적록색약
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt_rrb += 1

print(f'{cnt_rgb} {cnt_rrb}')