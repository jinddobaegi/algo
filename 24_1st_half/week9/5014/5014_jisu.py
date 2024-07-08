# 5014 스타트링크
from collections import deque
# 총 층수 F, 스타트링크 위치 G, 현재 위치 S, 위로 가는 수 U, 아래로 갈 수 있는 D
def bfs(S, cnt):
    q.append(S)

    while q:
        start = q.popleft()
        if 0 <= start - D < F and not visited:
            visited[start - D] = 1
            start = start - D
            cnt += 1
            q.append(start, cnt)





F, S, G, U, D = map(int, input().split())
visited = [0] * F
visited[S] = 1
# [0][0][0][0][0][0][0][0][0][1]

q = deque
min_v = 1e9
cnt = 0

