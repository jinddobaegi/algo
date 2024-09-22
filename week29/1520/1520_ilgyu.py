import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')
import heapq

n, m = map(int, input().split()) # 세로, 가로
area = [list(map(int, input().split())) for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def sol(i, j):
    pq = []
    heapq.heappush(pq, (-area[0][0], 0, 0))
    dp[0][0] = 1

    while pq:
        height, x, y = heapq.heappop(pq)

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < m and area[nx][ny] < area[x][y]:
                if dp[nx][ny] == 0:
                    heapq.heappush(pq, (-area[nx][ny], nx, ny))
                dp[nx][ny] += dp[x][y]
        # heapq에 담을 때 -를 붙여서 최대값부터 나오게함
        # 32에서 30이랑 20으로 갈 수 있는데
        # 그냥 bfs로하면 32 -> 20 순서로 방문해서
        # 20에 (32 -> 30 -> 25 -> 20)으로 간 값이 전달이 안됨
        # 최대힙을 쓰면 20보다 큰 수들을 다 방문하고 나서야 20에 갈 수 있음

dp = [[0] * m for _ in range(n)]
# dp[i][j] 값은 (i, j)까지 올 수 있는 방법의 수
# cnt = 0
sol(0, 0)
#
# for k in dp:
#     print(k)
# print(cnt)
# cnt가 17만 나와도 되는데 기본 bfs로하면 20이 나옴
print(dp[n-1][m-1])





