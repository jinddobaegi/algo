import sys
sys.stdin = open('input.txt')
from collections import deque

# visited 써서 같은 곳 재방문 하는 걸 없애야했음

di = [1, 0]
dj = [0, 1]
def game_start(i,j):
    q = deque()
    start = [i, j]
    q.append(start)
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        d = area[x][y]
        if d == -1:
            print('HaruHaru')
            return
        for k in range(2):
            next_x, next_y = x + d * di[k], y + d * dj[k]

            if 0 <= next_x < N and 0 <= next_y < N and visited[next_x][next_y] == False:
                if area[next_x][next_y] == -1:
                    print("HaruHaru")
                    return
                else:
                    q.append([next_x, next_y])
                    visited[next_x][next_y] = True

    print("Hing")

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
# print(visited)

game_start(0,0)
# print(area)
# 스택대신 재귀