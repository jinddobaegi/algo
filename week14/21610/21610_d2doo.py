# 마법사 상어와 비바라기
# 행과 열이 줄줄줄 이어지는 것 유의
# 근데 물복사버그 할 땐 이어지지 않음 ㅋㅋ;;

N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
cross = [[-1, -1], [-1, 1], [1, -1], [1, 1]]  # 대각선
# 2. 비바라기 시전하면 (N,1) (N,2) (N-1, 1) (N-1 2)에 비구름 생긴다(인덱스 맞추기)
cloud = [[N - 1, 0], [N - 2, 0], [N - 1, 1], [N - 2, 1]]

# M 만큼 이동합니다.
for _ in range(M):
    # 이동하는 방향 d(+1 된 상태로 주어지니까 아래에서 -1 해주기), 이동하는 거리 s
    d, s = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    clouds = []

    while cloud:
        y, x = cloud.pop()  # 조건 3-3
        # 1. d의 방향으로 s만큼 이동한다.
        ny, nx = (y + dy[d - 1] * s) % N, (x + dx[d - 1] * s) % N
        # 2. 방문한 곳에 1 더해준다.
        basket[ny][nx] += 1
        visited[ny][nx] = 1
        clouds.append([ny, nx])

    # 4. 물복사 버그 시전
    for ny, nx in clouds:
        for cy, cx in cross:
            my, mx = ny + cy, nx + cx
            # 얘는 행과 열이 연결되어있지 않음.
            if 0 <= my < N and 0 <= mx < N and basket[my][mx]:
                basket[ny][nx] += 1

    # 방문하지 않은 곳에서 물의 양이 2 이상인 바구니 찾아서 2 빼 버리기.
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and not visited[i][j]:
                basket[i][j] -= 2
                cloud.append([i, j])

# 이게 뭔 말인지 모르겠넹
print(sum(map(sum, basket)))
