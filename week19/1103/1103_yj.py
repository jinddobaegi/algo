import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)   # 제한없으니 recursion 에러남

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]  # 방문 여부를 통해 무한 반복 가능성 체크
dp = [[0] * M for _ in range(N)]
ans = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    for i in range(4):
        nx = x + dx[i] * int(arr[x][y])
        ny = y + dy[i] * int(arr[x][y])

        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 'H':  # 보드 범위 내에 있고 구멍이 아니라면
            if visited[nx][ny] == 1:   # 방문한 곳이라면 무한 루프 -> 종료
                print(-1)
                exit()

            if cnt + 1 > dp[nx][ny]:  # 더 많이 이동할 수 있는 경우에만 갱신
                dp[nx][ny] = cnt + 1
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0

dfs(0, 0, 0)
print(ans + 1)