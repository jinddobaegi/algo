N = int(input())
s_num = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

num = N * N
r = 0
c = 0
i = 0
s_idx = []

# 큰 수부터 아래, 오른쪽, 위쪽, 왼쪽 방향으로 돌면서 숫자 채워가기
while num != 0:
    arr[r][c] = num
    if num == s_num:  # 찾는 수라면
        s_idx = [r + 1, c + 1]

    # 다음 위치
    nr = r + dx[i]
    nc = c + dy[i]

    # 범위 벗어나거나 이미 채워져 있으면 방향 전환
    if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] != 0:
        i = (i + 1) % 4
        nr = r + dx[i]
        nc = c + dy[i]

    r = nr
    c = nc
    num -= 1

for i in arr:
    print(*i)

print(*s_idx)