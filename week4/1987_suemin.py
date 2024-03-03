# 알파벳
# 골드4

import sys

# 상하좌우 인접칸 이동 가능
# 새로 이동한 칸의 글자는 예전 글자랑 달라야함
# 지나온 칸의 글자를 저장하는 리스트 필요하고
# 지나온 칸을 체크하는 것 필요
# 좌측상단 시작, 최대몇칸 지나는지 쳌

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))
cnt = 0
# set이 더 효율적이고, 빠름
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global cnt
    cnt = max(cnt, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not board[nx][ny] in visited:
            visited.add(board[nx][ny])
            dfs(nx, ny, count+1)
            visited.remove(board[nx][ny])
visited.add(board[0][0])
dfs(0, 0, 1)
print(cnt)


# 99%에서 틀렸습니다 코드
# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline
#
# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# def recur(x, y, val):
#     if lst[x][y] in visited:
#         global ans
#         ans = max(ans, val)
#         return
#     visited.add(lst[x][y])
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if -1<nx<r and -1<ny<c:
#             recur(nx,ny, val+1)
#     visited.remove(lst[x][y])
#
# r,c = map(int, input().split())
# lst = [list(map(ord, list(input().rstrip()))) for _ in range(r)]
# ans = 0
# visited = set()
# recur(0,0,0)
# print(ans)