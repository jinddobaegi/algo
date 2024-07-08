import sys
sys.stdin = open("week14/21610/21610.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dist = []
for _ in range(M):
  direction, distance = map(int, input().split())
  dist.append((direction, distance))

# print(dist)

delta = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
cloud = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]

for dir, dis in dist:
    # 모든 구름이 di 방향으로 si칸 이동한다.
    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    new_cloud = []
    for x, y in cloud:
        nx, ny = (x + delta[dir][0] *dis) % N, (y + delta[dir][1] *dis) % N # 나머지 만큼이동해야 하므로 %N
        new_cloud.append((nx, ny))
        # print("append new_cloud = ", new_cloud)
        graph[nx][ny] += 1
    # print(new_cloud) 
    # 구름이 모두 사라진다.
    cloud = []
    # 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    for x, y in new_cloud:
        for dx, dy in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > 0:
                graph[x][y] += 1
    # 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for row in range(N):
        for col in range(N):
            if (row, col) not in new_cloud and graph[row][col] >= 2:
                graph[row][col] -= 2
                cloud.append((row, col))
                # print("append cloud = ", cloud)
    # new_cloud = []
    # print(new_cloud)
result = 0
for i in graph:
    result += sum(i)
  
print(result)

                



