# 바닥 장식
# 실버 4

import sys
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# 가로 세로 바닥 장식 개수
a = 0
b = 0

for i in range(N):
    for j in range(M):
        if j > 0 and board[i][j] == board[i][j-1] and board[i][j] == '-':
            continue
        elif board[i][j] == '-':
            a += 1

for i in range(N):
    for j in range(M):
        if i > 0 and board[i][j] == board[i-1][j] and board[i][j] == '|':
            continue
        elif board[i][j] == '|':
            b += 1

print(a+b)


