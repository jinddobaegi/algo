# 스타트링크
# 흠 BFS?
from collections import deque

def bfs(start):
    q = deque([start])

    cnt = [-1] * F
    cnt[start] = 0

    while q:
        now = q.popleft()

        if now == G - 1: # 도착
            return cnt[now]

        for i in range(2): # Up & Down 중 하나
            if i == 0:
                next_floor = now + U
            else:
                next_floor = now - D

            if 0 <= next_floor < F and cnt[next_floor] == -1: # 범위, 방문 여부 체크
                q.append(next_floor)
                cnt[next_floor] = cnt[now] + 1
    return 'use the stairs'				# 탐색을 다 해도 도착 못하면 문자열 반환

# 총 층수 : F, 강호 위치 : S, 가야하는 곳 : G, 업 : U, 다운: D
F, S, G, U, D = map(int, input().split())
print(bfs(S - 1))

# pypy -> 127880kb | 228ms
# python3 -> 71784KB | 536ms