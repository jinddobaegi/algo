import copy
from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def virus(copy_arr, i, j):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < M and copy_arr[ni][nj] == 0:
            copy_arr[ni][nj] = 2
            virus(copy_arr, ni, nj)

empty_lst = []
max_safe = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            empty_lst.append([i, j])

# 벽 세울 수 있는 조합 만들기
for empty in combinations(empty_lst,3):
    copy_arr = copy.deepcopy(arr)

    # 벽 세우기
    for i, j in empty:
        copy_arr[i][j] = 1

    # 바이러스 전파
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 2:
                virus(copy_arr, i, j)

    # 안전 영역 체크
    safe = 0
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 0:
                safe += 1

    max_safe = max(safe, max_safe)

print(max_safe)