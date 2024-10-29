from collections import deque

N, M = map(int, input().split()) # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
land = dict()
land_lst = []

# 섬 구분
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
land_num = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            q = deque([(i, j)])
            visited[i][j] = 1
            land[(i, j)] = land_num
            land_lst.append((i, j, land_num))

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + di[k]
                    ny = y + dj[k]

                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
                        land[(nx, ny)] = land_num
                        land_lst.append((nx, ny, land_num))
            land_num += 1

land_dist = []
for x, y, landnum in land_lst:
    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]
        dist = 0

        while True:
            if not (0 <= nx < N and 0 <= ny < M):
                break
            t_land = land.get((nx, ny))
            if landnum == t_land:
                break
            if t_land == None:
                nx = nx + di[k]
                ny = ny + dj[k]
                dist += 1
                continue
            if dist < 2:
                break

            land_dist.append((dist, landnum, t_land))
            break

land_dist = sorted(land_dist, reverse=True)

result = 0
cnt = land_num - 1
parents = [i for i in range(land_num)]
temp = 0

def find(k) :
    if k != parents[k] :
        parents[k] = find(parents[k])
    return parents[k]

def union(x, y) :
    x = find(x)
    y = find(y)
    parents[y] = x

while cnt:
    try :
        distance, a, b = land_dist.pop()
    except :
        temp = 1
        break

    if find(a) != find(b) :
        union(a, b)
        result += distance
        cnt -= 1

if temp == 1:
    print(-1)
else:
    print(result)