# 아기 상어

# N*N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다.
# 공간은 1*1크기의 정사각형 칸으로 나누어져 있다. 
# 한칸에는 물고기가 최대 1마리 존재한다.

# 아기 상어와 물고기 모두 크기를 가지고있고, 이 크기는 자연수이다.
# 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸 씩 이동한다.

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 잇다.
# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

# 아기 상어가 어디로 이동할 지 결정하는 바법은 아래와 같다.
# 1. 더이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러간다.
# 3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
#     - 거리는 아기 상어가 잇는 칸에서 물고기가 있는 칸으로 이동할 때 , 지나야 하는 칸의 개수의 최솟값이다.
#     - 거리가 가까운 물고가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면,
# 이동과 동시에 물고기를 먹는다. 물고리를 먹으면, 그 칸은 빈 칸이 된다.

# 아기 상어는 자신의 크기와 은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이된다.
# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고리를 잡아 먹을 수 있는지 구하는 프로그램을 작성하시오.

# 입력 
# 척째 줄에 공간의 크기 N(2<= N <= 20) 이 주어진다.
# 둘재 줄부터 N개의 줄에 공간의 상태가 주어진다.
# 공간의 상태는 0,1,2,3,4,5,6,9로 이루어져 이속, 아래와 같은 의미를 가진다.
# - 0: 빈 칸
# - 1,2,3,4,5,6: 칸에 있는 물고기의 크기
# - 9: 아기 상어의 위치

# 아기 상어는 공간에 한 마리 있다.

# 출력
# 첫 째줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

import sys
sys.stdin = open('week18/16236/16236.txt')
input = sys.stdin.readline

# N = int(input())
# graph = [list(map(int, input().split())) for _ in range(N)]

# for _ in graph:
#     print(_)

# 물고기의 크기가 상어의 크기보다 작다면 먹으러간다.
# 같은 크기의 물고기가 있다면 최소경로에 있는 물고기를 먼저 먹으러간다.
# 상어는 2로 시작하고 자신의 크기만큼 물고

# 9를 먼저 찾고 0으로 초기화
# 이동은 상어의 크기보다가 작거나 같은 경우만 가능 -> 큰경우는 이동불가
# 먹을 수있는 것중에 최소경로를 찾아 먹기 -> 상어 진화 및 유지 -> 똑같이 최소경로 찾아 먹기
# 경로의 길이만큼 시간초 추가 +1 씩
# 0만 남거나 먹을 수 없는 것들만 남을때 까지 반복
# 시간 출력
# def check_load():
    

# def check_size(shark):
#     start_x, start_y = shark
#     min_load = 20*20*20
#     for i in range(N):
#         for j in range(N):
#             if graph[i][j] < shark_size:
#                 min_load = min(min_load, check_load(start_x,start_y)) #최소경로를 찾고 그중 제일 작은경로의 시간을 리턴/ 그리고 그 정점을 0으로 초기화 / 그리고 상어크기 증가
#             if min_load == check_load(start_x,start_y):
#                 graph[start_x][start_y] = 0
#                 new_shark = (i,j)
                
#                 check_size(new_shark)

    

# shark_size = 2
# shark = ()
# # 아기 상어의 위치 찾기
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 9:
#             shark = (i, j)
#             graph[i][j] = 0
#             break
# # print(shark)
# check_size()

from collections import deque

def bfs(shark_x, shark_y, shark_size):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(shark_x, shark_y, 0)])
    visited = [[False] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    fish_list = []

    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
                    
                    if 0 < graph[nx][ny] < shark_size:
                        fish_list.append((dist + 1, nx, ny))
    
    fish_list.sort()
    return fish_list

def solve():
    shark_size = 2
    fish_eaten = 0
    total_time = 0
    shark_x, shark_y = shark

    while True:
        fish_list = bfs(shark_x, shark_y, shark_size)
        
        if not fish_list:
            break
        
        dist, fish_x, fish_y = fish_list[0]
        graph[fish_x][fish_y] = 0
        total_time += dist
        fish_eaten += 1
        
        if fish_eaten == shark_size:
            shark_size += 1
            fish_eaten = 0
        
        shark_x, shark_y = fish_x, fish_y
    
    print(total_time)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

shark = ()
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            shark = (i, j)
            graph[i][j] = 0
            break

solve()

