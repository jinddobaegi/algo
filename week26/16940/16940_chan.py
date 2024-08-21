import sys
sys.stdin = open("week26/16940/16940.txt")
input = sys.stdin.readline
from collections import deque
from pprint import pprint

def bfs(graph, v):
    visited = [False] * len(graph)
    visited[v] = True
    queue = deque([v])
    linelist = []
    # print(linelist)
    while queue:
        node = queue.popleft()
        linelist.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return linelist


N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs_result = list(map(int, input().split()))

linelist = bfs(graph, 1)
# print(linelist)

if linelist == bfs_result:
    print(1)
else:
    print(0)