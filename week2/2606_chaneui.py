import sys
sys.stdin = open("2606.txt")

from collections import deque

def BFS():
    Q = deque([1])
    visited[1] = 1
    while Q:
        onstart = Q.popleft()
        for select in graph[onstart]:
            if not visited[select]:
                visited[select] = 1
                Q.append(select)

number = int(input())
N = int(input())
graph = [[] for _ in range(number+1)]
visited = [0]* (number+1)
for i in range(N):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS()
result = sum(visited) - 1
print(int(result))








    






