N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
max_sum = 0
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# dfs를 통해 모든 경우를 계산
def dfs(i, j, cnt, c_sum):
    global max_sum
    # 테트로미노가 완성된 경우
    if cnt == 4:
        max_sum = max(max_sum, c_sum)
        return
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt + 1, c_sum + arr[ni][nj])
                visited[ni][nj] = 0

# ㅜ 블럭의 경우 + 블럭 만들고 하나씩 빼는 방식으로 처리
def block(i, j, c_sum):
    global max_sum
    temp = []

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < M:
            c_sum += arr[ni][nj]
            # 하나씩 빼면서 계산하기 위해 temp 배열에 추가
            temp.append(arr[ni][nj])
        else:   # 범위 벗어나는 경우에는 0 추가해서 계산
            temp.append(0)

    for k in range(4):
        max_sum = max(max_sum, c_sum - temp[k])

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        block(i, j, arr[i][j])
        visited[i][j] = 0

print(max_sum)