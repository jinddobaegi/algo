from sys import stdin

input = stdin.readline


def flip(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            A[i][j] ^= 1  # XOR 연산: 같을 땐 0, 다를 땐 1을 반환


N, M = map(int, input().split())
A = list(list(map(int, list(input().rstrip()))) for _ in range(N))
B = list(list(map(int, list(input().rstrip()))) for _ in range(N))

res = 0
if (N < 3 or M < 3) and (A != B):
    res = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                flip(i, j)
                res += 1

        # 한 줄을 바꿔도 다르면 가능성 x
        if A[i] != B[i]:
            res = -1
            break

print(res if A==B else -1)