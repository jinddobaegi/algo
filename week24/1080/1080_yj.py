N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

# 0 → 1, 1 → 0 바꾸는 함수
def turn(x, y):
    for k in range(x, x+3):
        for l in range(y, y+3):
            if A[k][l] == 0:
                A[k][l] = 1
            else:
                A[k][l] = 0

            # 1. A[k][l] = 1 - A[K][l]
            # 2. A[k][l] ^= A[K][l]

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            turn(i, j)

if A != B:
    print(-1)
else:
    print(cnt)