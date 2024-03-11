from collections import deque

garo, sero, num = map(int, input().split())

def bfs(hight,row,col):
  Q = deque([hight,row,col])

  while Q:
    if not Q:
      return
    delta = [(1,0,-1),(0,0,-1)]
  

graph = [[input().split() for _ in range(sero)] for _ in range(num)] 
visited = [[[0] for _ in range(sero)] for _ in range(num)] 
print(graph)
for i in graph:
  print(i)

print(graph[0][0][0])

bfs(0,0,0)