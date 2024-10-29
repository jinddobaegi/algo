R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기
cleaner = []
for i in range(R):
    if arr[i][0] == -1:
        cleaner.append((i, 0))

# 미세먼지 확산
def spread():
    diff = [[0] * C for _ in range(R)]
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        diff[ni][nj] += arr[i][j] // 5
                        diff[i][j] -= arr[i][j] // 5
    for i in range(R):
        for j in range(C):
            arr[i][j] += diff[i][j]

# 공기청정기 반시계 방향
def up_clean():
    i, j = cleaner[0]
    di, dj = [0, -1, 0, 1], [1, 0, -1, 0]
    dir = 0
    i, j = i, 1
    prev = 0
    while True:
        ni, nj = i + di[dir], j + dj[dir]
        if (i, j) == cleaner[0]:
            break
        if not (0 <= ni < R and 0 <= nj < C):
            dir += 1
            continue
        arr[i][j], prev = prev, arr[i][j]
        i, j = ni, nj

# 공기청정기 시계 방향
def down_clean():
    i, j = cleaner[1]
    di, dj = [0, 1, 0, -1], [1, 0, -1, 0]
    dir = 0
    i, j = i, 1
    prev = 0
    while True:
        ni, nj = i + di[dir], j + dj[dir]
        if (i, j) == cleaner[1]:
            break
        if not (0 <= ni < R and 0 <= nj < C):
            dir += 1
            continue
        arr[i][j], prev = prev, arr[i][j]
        i, j = ni, nj

for _ in range(T):
    spread()
    up_clean()
    down_clean()

ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            ans += arr[i][j]

print(ans)