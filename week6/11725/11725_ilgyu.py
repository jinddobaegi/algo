import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
# print(graph)
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# for m in graph:
#     print(m)

visited = [0] * (N+1)

# 1. dfs 재귀풀이 / 시간이 너무 오래 걸림
# def dfs(s):
#     for i in graph[s]:
#         if visited[i] == 0:
#             visited[i] = s
#             dfs(i)
# dfs(1)
# for x in range(2, N+1):
#     print(visited[x])


# 2. bfs풀이
q = deque()
q.append(1)
def bfs(visited):
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if visited[next] == 0:
                visited[next] = cur
                q.append(next)
bfs(visited)
# print(visited)
for x in range(2, N+1):
    print(visited[x])
# visited[1] = 6 찍히는 이유가
# graph자체가 부모 - 자식 관계를 표현했다기 보다는 연결상태를 나타낸거여서
# bfs로 체크하는 과정에서 1 -> 6도 체크하고 6 -> 1도 체크해서 그럼
