# 효율적인 해킹
from collections import deque

def bfs(s):
    q = deque()
    q.append(s)
    cnt = 0

    visited = [0] * (N + 1)
    visited[s] = 1

    while q:
        x = q.popleft()
        for next in trust[x]:
            if not visited[next]:
                visited[next] = 1
                q.append(next)
                cnt += 1
    return cnt

N, M = map(int, input().split())
trust = [[] for _ in range(N + 1)]

# 트리 만들기
for _ in range(M):
    a, b = map(int, input().split())
    trust[b].append(a)

# 인덱스를 가지고 있는 컴퓨터가 몇 대를 해킹 할 수 있는지 저장
ans = [0]
for s in range(1, len(trust)):
    ans.append(bfs(s))

# 컴퓨터가 최대 해킹 가능 컴퓨터라면 res에 저장 후
res = []
for i in range(1, len(ans)):
    if max(ans) == ans[i]:
        res.append(i)

# 정렬하고
res.sort()
# 언패킹으로 프린트
print(*res)