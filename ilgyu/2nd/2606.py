import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(s, V, visited, adj_m):
    global cnt
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        t = q.popleft()
        for w in range(1, 1+V):
            if adj_m[t][w] == 1 and not visited[w]:
                q.append(w)
                visited[w] = True
                cnt += 1


V = int(input()) # 컴퓨터의 수
E = int(input()) # 연결되어 있는 컴퓨터 쌍의 수 ( 간선 수 )
adj_m = [[0]*(V+1) for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    a, b = map(int, input().split())
    adj_m[a][b] = 1
    adj_m[b][a] = 1
cnt = 0
bfs(1, V, visited, adj_m)
print(cnt)