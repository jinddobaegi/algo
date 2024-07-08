import sys
sys.stdin = open('input.txt')
from collections import deque
def moving(s):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while q:
        cur, cnt = q.popleft()
        if cur == g:
            return cnt
        for next in ([cur + u, cur - d]):
            if 1 <= next <= f and visited[next] == False: # 1층부터 시작이니까 관습적으로 0 <= 하면안됨
                q.append((next, cnt + 1))
                visited[next] = True

    return 'use the stairs'

f, s, g, u, d = map(int, input().split()) # 총/ 현재/ 목표/ 위 / 아래
visited = [False] * (f+1)

print(moving(s))