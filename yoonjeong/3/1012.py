import sys
sys.setrecursionlimit(10**6)

T = int(input())

def dfs(i, j):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < M and 0 <= nj < N and arr[nj][ni] == 1:
            arr[nj][ni] = -1
            dfs(ni, nj)

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)