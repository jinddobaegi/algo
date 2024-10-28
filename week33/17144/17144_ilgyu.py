import sys
sys.stdin = open('input.txt')
import copy

R, C, T = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(R)]

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
def spread():
    board = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if area[i][j] != -1 and area[i][j] != 0:
                res = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and area[ni][nj] != -1:
                        board[ni][nj] += area[i][j] // 5
                        res += area[i][j] // 5
                area[i][j] -= res

    for i in range(R):
        for j in range(C):
            area[i][j] += board[i][j]
# 공기청정기 위쪽
def air_up(a, area):
    x, y = a, 1
    idx = 0
    temp = 0
    while True:
        nx, ny = x + di[idx], y + dj[idx]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            idx = (idx+1) % 4
            continue

        if x == a and y == 0:
            break
        area[x][y], temp = temp, area[x][y]
        x, y = nx, ny

def air_down(b, area):
    x, y = b, 1
    idx = 0
    temp = 0
    while True:
        nx, ny = x + di[idx], y + dj[idx]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            idx = (idx + 3) % 4
            continue

        if x == b and y == 0:
            break
        area[x][y], temp = temp, area[x][y]
        x, y = nx, ny


clean = []
# 0. 청소기 위치
for i in range(R):
    for j in range(C):
        if area[i][j] == -1:
            clean.append([i, j])
a = clean[0][0]
b = clean[1][0]

for _ in range(T):
    spread()
    air_up(a, area)
    air_down(b, area)

ans = 0
for x in area:
    ans += sum(x)
print(ans+2)
