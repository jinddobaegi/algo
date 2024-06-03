# 테르로미노
# max 갱신 dfs

# 한 줄로 이을 수 있는 친구
def once_cal(i, j, now, cnt):
    global max_v
    if cnt == 4:
        max_v = max(max_v, now)
        return
    for num in range(4):
        ni = i + di[num]
        nj = j + dj[num]
        # 에러처리(?)
        if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj]:
            continue
        visited[ni][nj] = 1  # 방문
        once_cal(ni, nj, now + paper[ni][nj], cnt + 1)
        visited[ni][nj] = 0  # 여러경우를 탐색하기위해 리턴으로 빠져나오면 false 처리


# ㅗ
def twice_cal(i, j):
    global max_v
    now = paper[i][j]
    arr = []

    for num in range(4):
        ni = i + di[num]
        nj = j + dj[num]
        # 에러처리(?)
        # if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj]: <- 이거 안됨
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue
        arr.append(paper[ni][nj])

    # 인접해 있는 4방향중 제일 작은거 빼고 더해버리면 ㅗ, ㅓ, ㅏ, ㅜ 나옴
    if len(arr) == 4:
        max_v = max(max_v, now + sum(arr) - min(arr))

    # 꼭다리에 있어서 인접한게 3개인 경우
    elif len(arr) == 3:
        max_v = max(max_v, now + sum(arr))
    return


N, M = map(int, input().split())  # 세로 N, 가로 M
paper = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

max_v = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        once_cal(i, j, paper[i][j], 1)
        visited[i][j] = 0
        twice_cal(i, j)

print(max_v)
