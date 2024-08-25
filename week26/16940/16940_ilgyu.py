import sys
input = sys.stdin.readline
from collections import deque


def bfs(num):
    q = deque()
    q.append(num)
    idx = 1
    visited = [False] * (n+1)
    visited[num] = True

    while q:
        node = q.popleft()

        child = []
        for next in tree[node]:
            if visited[next] == False:
                child.append(next)

        # lst.sort() => 원본 lst를 직접 수정
        # x = sorted(lst) => 원본 lst는 수정하지 않음
        if sorted(order[idx: idx+len(child)]) != sorted(child):
            return False
        else:
            # tree[node]에서 말고 order순서대로 q에 넣어야함
            for next in order[idx: idx+len(child)]:
                visited[next] = True
                q.append(next)
                idx += 1
    return idx


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
order = list(map(int, input().split()))

a = bfs(1)
# print(a)
if a == False:
    print(0)
else:
    print(1)