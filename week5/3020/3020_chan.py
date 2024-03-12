N, H = map(int, input().split())

# 시간초과

# 첫번째 장애 물은 항상 석순 N 은 짝수
# 장애물을 파괴하는 최솟 값과 그 수
graph = [0]*H

# print(graph)
check = []
for _ in range(N):
  check.append(int(input()))

for i in range(N):
  if i % 2 == 0:
    for j in range(check[i]):
      graph[H-1-j] += 1
  else:
    for j in range(check[i]):
      graph[j] += 1

result = min(graph)
count = graph.count(result)
print(result, end=" ")
print(count)