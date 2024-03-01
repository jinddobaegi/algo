import sys
sys.stdin = open('input.txt')
from collections import deque
def bfs(s_row, s_col):
    global answer
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    stack = set([(s_row, s_col, board[s_row][s_col])])
    while stack:
        i, j, ans = stack.pop()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0<=ni<R and 0<=nj<C and board[ni][nj] not in ans:
                stack.add((ni, nj, ans + board[ni][nj]))
                answer = max(answer, len(ans)+1)


R, C = list(map(int, input().split())) #R세로 C가로
board = [list(map(str, input())) for _ in range(R)]
answer = 1
bfs(0,0)
print(answer)

