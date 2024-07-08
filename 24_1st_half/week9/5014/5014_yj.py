import sys
from collections import deque
input = sys.stdin.readline

# F = 전체 층, G = 스타트링크 위치, S = 지금 있는 곳, U = 위로 U층, D = 아래로 D층
F, S, G, U, D = map(int, input().split())

# 숨바꼭질 문제랑 살짝 비슷한듯..? 근데 경로 저장할 필요 X

cnt = [0] * (F + 1)
ans = 0

def bfs():
    global ans
    q = deque()
    q.append(S)
    cnt[S] = 1  # 시작 층은 다시 탐색할 필요 X

    while q:
        c = q.popleft()
        d = [c+U, c-D]

        if c == G:  # 도착한 경우
            ans = cnt[c] - 1
            break

        for i in d:
            if 0 < i <= F and cnt[i] == 0:
                cnt[i] = cnt[c] + 1
                q.append(i)

    if cnt[G] == 0:
        ans = "use the stairs"

bfs()

print(ans)