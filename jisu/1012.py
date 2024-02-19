di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())
    cabbage = [list(map(int, input().split())) for _ in range(K)]
    field = [[0] * N for _ in range(M)]

    for i in range(len(cabbage)): # field 채우기
        a, b = cabbage[i]
        field[a][b] = 1

    cnt = 0
    stack = []

    for i in range(M):
        for j in range(N):
            for l in range(4):
                ni, nj = i + di[l], j + dj[l]
            if 0 <= ni < M and 0 <= nj < N:
                field[i][j] = 0
                cnt -= field[i][j]

    print(f'#{tc} {cnt}')