import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
cnt = 0

def check(row):
    for r in range(row):
        if arr[r] == arr[row] or abs(r - row) == abs(arr[r] - arr[row]):
            return False

    return True

def sol(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for i in range(N):
        arr[row]= i
        if check(row):
            sol(row + 1)

sol(0)
print(cnt)


# 시간초과
# import sys
# input = sys.stdin.readline
#
# N = int(input())
# arr = [[0]*N for _ in range(N)]
# cnt = 0
#
# def check(x, y):
#     dx = [1, 1, -1, -1, 1, -1]
#     dy = [0, 1, 1, -1, -1, 0]
#
#     for i in range(6):
#         nx, ny = x, y
#         while 0 <= nx < N and 0 <= ny < N:
#             nx += dx[i]
#             ny += dy[i]
#             if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
#                 return 0
#     return 1
#
# def sol(row):
#     global cnt
#     if row == N:
#         cnt += 1
#         return
#     for i in range(N):
#         if check(row, i):
#             arr[row][i] = 1
#             sol(row + 1)
#             arr[row][i] = 0
#
# sol(0)
# print(cnt)