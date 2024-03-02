# 연결 요소의 개수
# pypy3로 제출해야 시간초과가 안남

import sys
sys.setrecursionlimit(100000)

def dfs(contact, i, visited):
    visited[i] = 1
    for j in contact[i]:
        if not visited[j]:
            dfs(contact, j, visited)

N, M = map(int, input().split())
contact = [[] for _ in range(N+1)]
cnt = 0
visited = [0] * (N+1)

# 방향이 없는 연결
for _ in range(M):
    u, v = map(int, input().split())
    contact[u].append(v)
    contact[v].append(u)

for i in range(1, N+1): # 0은 어차피 없는 애니까
    # print(f'i={i}')
    if not visited[i]:
        dfs(contact, i, visited)
        cnt += 1

print(cnt)