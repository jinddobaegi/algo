import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    d = int(board[x][y])

    for k in range(4):
        nx, ny = x + d * di[k], y + d * dj[k]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'H' and dp[nx][ny] < cnt + 1:
            # dp[nx][ny]는 현재까지 nx, ny 위치에 도달한 최대 이동 횟수
            # cnt + 1은 현재 위치에서 nx, ny로 이동했을 때의 이동 횟수
            # 이동할 수 있는 최대 값을 구하는 거니까 더 작은 경우는 고려할 필요 없음
            # 현재까지 이동 횟수가 cnt이고 내가 다음에 갈 위치가 nx, ny인데 만약 이미 dp[nx][ny]에 값이 있고 그게 cnt +1 (= 해당 위치로 이동했을 때의 움직임 횟수)보다 크다면
            # 내가 원하는건 최대한 많이 움직인 횟수니까 검사할 필요가 없음
            if visited[nx][ny]:
                print(-1)
                exit()

            else:
                visited[nx][ny] = True
                dp[nx][ny] = cnt + 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = False # nx, ny에 도달할 수 있는 방법이 여러가지니까 재귀돌려야해서


n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]

dp = [[0] * m for _ in range(n)] # dp[i][j]는 (i, j) 위치까지 몇번만에 갔는지를 뜻함
visited = [[False] * m for _ in range(n)]
ans = 0
dfs(0, 0, 1)
print(ans)
