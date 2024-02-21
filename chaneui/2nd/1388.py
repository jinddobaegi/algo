import sys
sys.stdin = open("1388.txt")

def DFS(row, col, direction):
  count = 0
  if row >= S or col >= G or visited[row][col] == 1:
    return
  if (direction == '-' and graph[row][col] != '-') or (direction == '|' and graph[row][col] != '|'):
    return
  visited[row][col] = 1

  if direction == '-':
    DFS(row, col+1, direction)
  else:
    DFS(row+1, col, direction)
  count += 1

  return count


S, G = map(int, input().split())
graph = [input() for _ in range(S)]
# print(graph)
visited = [[0]*G for _ in range(S)]
count = 0
for i in range(S):
  for j in range(G):
    if not visited[i][j] == 1:
      count += DFS(i, j, graph[i][j])
print(count)
