def dfs(i):
  for j in graph[i]:
    if visited[j] == 0:
      visited[j] = 1
      dfs(j)
    
points, lines = map(int, input().split())
graph = [[] for _ in range(points+1)]
visited = [0] * (points+1)
count = 0
for _ in range(lines):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, points+1):
    if visited[i] == 0:
      dfs(i)
      count += 1
print(count)