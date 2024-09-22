# 내리막 길
# D(FS + P)
# pypy로 하면 틀림
import sys
sys.setrecursionlimit(10 ** 7)

def DFS(i, j):
     if i == M - 1 and j == N - 1: # 도착지점에 도착
         return 1
     if dp[i][j] == -1:
        dp[i][j] = 0 # 방문 표시
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < M and 0 <= nj < N and maps[ni][nj] < maps[i][j]: # 범위 내에 있고 낮으면
                dp[i][j] += DFS(ni, nj)
     return dp[i][j]

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
di = [0, 0, 1, -1] # 세로
dj = [1, -1, 0, 0] # 가로

print(DFS(0, 0))