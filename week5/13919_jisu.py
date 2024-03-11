from collections import deque

# 최소 거리
# 가는 길?
def bfs(now, K):
    answer.append(now)
    q.append(now)
    while q:
        x = q.popleft()
        for a in [x - 1, x + 1, x * 2]:
            # print(a)
            if a == K and max_c <= max(max_c, cnt): # 어떻게 하지?
                answer.append(a)
                break
            else:
                q.append(a)

N, K = map(int, input().split())
answer = []
q = deque()
max_c = 0 # 어떻게 하면 좋지?

bfs(N, K)