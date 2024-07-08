N = int(input())   # 지도의 크기
arr = []
home_lst = []
home_cnt = 0  # 단지내 집의 수

for _ in range(N):
    arr.append(list(map(int, input())))

def dfs(i, j):
    global home_cnt
    home_cnt += 1
    arr[i][j] = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
            dfs(ni, nj)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_cnt = 0  # 단지내 집의 수 초기화
            dfs(i, j)
            home_lst.append(home_cnt)

print(len(home_lst))
home_lst.sort()
for i in home_lst:
    print(i)