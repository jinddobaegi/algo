N, M = map(int, input().split())  # 격자 크기, 이동 횟수
arr = list(list(map(int, input().split())) for _ in range(N))

di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]   # 비구름

for i in range(M):
    d, s = map(int, input().split())
    c_lst = []
    visited = [[0] * N for _ in range(N)]

    # 1. 모든 구름이 d 방향으로 s칸 이동
    for j in cloud:
        nx = j[0] + di[d-1] * s
        ny = j[1] + dj[d-1] * s
        nx %= N
        ny %= N
        c_lst.append([nx, ny])

        # 2. 구름 있는 칸 바구니에 저장된 물의 양 1 증가
        arr[nx][ny] += 1
        visited[nx][ny] += 1

    # 3. 구름이 모두 사라짐
    cloud = []

    # 4. 물복사버그 마법 시전 !
    for x, y in c_lst:
        for idx in range(1, 8, 2):
            nx = x + di[idx]
            ny = y + dj[idx]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0:
                arr[x][y] += 1

    # 5. 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양 2 감소
    for i in range(N):
        for j in range(N):
            # 3에서 구름이 사라진 칸이 아니어야 함
            if arr[i][j] >= 2 and visited[i][j] == 0:
                arr[i][j] -= 2
                cloud.append([i, j])

w_sum = 0
for i in range(N):
    for j in range(N):
        w_sum += arr[i][j]

print(w_sum)