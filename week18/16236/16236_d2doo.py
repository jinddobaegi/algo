from collections import deque

def bfs(time, i, j):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    # lst = deque() # 먹을 수 있는 것들 넣는 리스트
    lst = []
    q.append([time, i, j])
    visited[i][j] = 1

    while q:
        time, i, j = q.popleft()

        for num in range(4):
            ni = i + di[num]
            nj = j + dj[num]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                # 먹을게 없거나(?) 크기가 같으면 이동만 해줌(시간 추가)
                if arr[ni][nj] == 0 or arr[ni][nj] == shark:
                    q.append([time + 1, ni, nj])
                    visited[ni][nj] = 1
                # 먹을게 있으면 리스트에 추가
                elif 0 < arr[ni][nj] < shark:
                    lst.append([time + 1, ni, nj])
                    visited[ni][nj] = 1

    # 리스트가 비었을 때
    if len(lst) == 0:
        return 0
    else:
        return lst.sort()


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            i = x
            j = y
shark = 2 # 상어 크기
eat = 0 # 먹은 횟수
time = 0 # 이동 횟수(?)

while True:
    arr[i][j] = 0 # 첫 아기상어 위치 0
    ans = bfs(0, i, j)
    # 더이상 먹을게 없다면 (종료조건)
    if ans == 0:
        print(time)
        break
    eat += 1
    # 아기상어가 자신의 크기만큼 먹으면(?)
    if shark == eat:
        shark += 1
        eat = 0

    i = ans[0][1] # TypeError: 'NoneType' object is not subscriptable
    j = ans[0][2]
    time += ans[0][0]