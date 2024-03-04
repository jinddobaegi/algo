# 아직 푸는 중입니당
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
max_c = 0
cnt = 0

def dfs(i, j):
    global max_c, cnt
    # if cnt > max_c:
    #     max_c = cnt
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        
        # ???
        # if 0 <= ni < R and 0 <= nj < C and visited[] == 0:
            # dfs(ni, nj)
            # cnt += 1

dfs(0, 0)