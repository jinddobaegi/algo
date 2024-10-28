import sys
sys.stdin = open('input.txt')
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
#
# for m in area:
#     print(m)

# n*m 최대 100 => 그냥 완탐?
# 1. 다리의 수는 섬의수 -1 개
# 2. 다리의 조합을 찾아서 모든 섬이 연결되는지 확인
# 다리가 되는지 어떻게 판별?
# 걍 풀로 돌려도 27,907,200  1초면됨

bridge = []
def horizon(i, j): # ㅡ
    res = []
    for x in range(j, m):
        if area[i][x] == 1:
            break
        res.append([i, x])
    return res

def vertical(i, j): # ㅣ
    res = []
    for x in range(i, n):
        if area[x][j] == 1:
            break
        res.append([x, j])
    return res

# 가로다리 찾기
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            if j == 0:
                if len(horizon(i, j)) <= 1:
                    continue
                else:
                    bridge.append(horizon(i, j))
            else:
                if area[i][j-1] == 1: # 바로 옆이 1이면 다리시작
                    if len(horizon(i, j)) <= 1:
                        continue
                    else:
                        bridge.append(horizon(i, j))

# 세로다리 찾기
for i in range(n):
    for j in range(m):
        if area[i][j] == 0:
            if i == 0:
                if len(vertical(i, j)) <= 1:
                    continue
                else:
                    bridge.append(vertical(i, j))
            else:
                if area[i-1][j] == 1:
                    if len(vertical(i, j)) <= 1:
                        continue
                    else:
                        bridge.append(vertical(i, j))

print(len(bridge))

# 섬 개수 찾기
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

cnt = 0 # 섬 개수
visited = [[False] * m for _ in range(m)]
def find(i, j):
    global cnt
    q = deque()
    q.append([i, j])
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and area[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = True

    cnt += 1

for i in range(n):
    for j in range(m):
        if area[i][j] == 1 and not visited[i][j]:
            find(i, j)

# print(cnt)

cases = combinations(bridge, cnt-1)
# ... 모르겠음 ...