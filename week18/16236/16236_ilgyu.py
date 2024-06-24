import sys
sys.stdin = open('input.txt')
from collections import deque

# 우선순위가 맨위, 맨왼쪽이니까 델타를 조정해줘야함
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def bfs(i, j, size):
    q = deque()
    q.append([i, j])
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    visited[i][j] = True
    fishes = [] # 먹을 수 있는 물고기칸 저장용 리스트

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if area[nx][ny] <= size: # 지날 수 있는 좌표들만 q에 저장
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    if 0 < area[nx][ny] < size: # 지날 수 있는 애들중 사이즈가 작다면 먹기가능 = fihses에 저장
                        fishes.append([distance[nx][ny], nx, ny])

    if fishes:
        fishes.sort() # 저장할 떄 distance부터 넣어서 가장 가까운 순으로 정렬하려고
        # print(fishes[0]) # 각 bfs마다 먹을 수 있는 애들을 fishes에 저장하고
                         # 어차피 내가 이동할 곳은 가장 가까이있는 물고기의 위치니까 fishes[0]만 뽑ㅇ면 됨
        return fishes[0]
    else:
        return None

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

# 1. bfs를 통해 먹을 수 있는 물고기와 해당 물고기까지의 거리를 구해서 리스트에 저장
# 2. while문으로 1에서 구한 리스트를 털면서 정답도출
size = 2
# 1. 현재 상어 위치특정짓기
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if area[i][j] == 9:
            x, y = i, j
            area[i][j] = 0

ans = 0
size_cnt = 0

# 시작지점에서 가장 가까운 거리(먹을 수 있는 곳)로 이동하면서
# 이동한 지점에서 BFS를 새로 돌리는 방식

while True:
    result = bfs(x, y, size)
    if result is None:
        break
    dist, nx, ny = result

    ans += dist
    area[nx][ny] = 0 # 해당 좌표의 물고기는 먹었으니까 0으로 처리
    x, y = nx, ny # 해당 좌표로 이동처리
    size_cnt += 1
    if size_cnt == size:
        size += 1
        size_cnt = 0

print(ans)
