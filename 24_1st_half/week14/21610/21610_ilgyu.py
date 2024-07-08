import sys
sys.stdin = open('input.txt')
from collections import deque

def cloud_move(d, s):
    directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
                  (0, 1), (1, 1), (1, 0), (1, -1)]

    dx, dy = directions[d - 1]

    for i in range(len(cloud)):
        cloud[i][0] = (cloud[i][0] + dx * s) % n
        cloud[i][1] = (cloud[i][1] + dy * s) % n

        if cloud[i][0] < 0:
            cloud[i][0] += n
        if cloud[i][1] < 0:
            cloud[i][1] += n

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
order = [] # [[1, 3], [3, 4], [8, 1], [4, 8]]
for _ in range(m):
    d, s = map(int, input().split())
    order.append([d, s])
# print(order)

# 1. order에 있는 명령대로 cloud들을 이동시킴
for i in range(m):
    d, s = order[i]
    cloud_move(d, s) # 구름이동
    # print(cloud)
    for j in range(len(cloud)):
        x, y = cloud[j]
        area[x][y] += 1 # 구름위치에 물 +1

    # 2. 물복사
    di = [-1, -1, 1, 1]
    dj = [-1, 1, 1, -1]

    for j in range(len(cloud)):
        x, y = cloud[j]
        water_cnt = 0
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < n and area[nx][ny] > 0:
                water_cnt += 1
        area[x][y] += water_cnt

    old_clouds = set(tuple(c) for c in cloud) # 기존 구름ㅈ ㅓ장
    cloud = [] # 새 구름통

    for l in range(n):
        for p in range(n):
            if area[l][p] >= 2 and (l, p) not in old_clouds:
                cloud.append([l, p])
                area[l][p] -= 2
# print(area)
ans = 0
for i in range(n):
    for j in range(n):
        ans += area[i][j]
print(ans)
