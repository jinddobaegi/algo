import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(input())
_map = [list(map(int, input())) for _ in range(n)]
# print(_map)
visited = [[False] * n for _ in range(n)]
# print(visited)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(i,j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    cnt = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < n and 0 <= ny < n and _map[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])
                cnt += 1

    return cnt
ans_list = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and _map[i][j] == 1:
            ans = bfs(i, j)
            ans_list.append(ans)


ans_list.sort()
print(len(ans_list))
for num in ans_list:
    print(num)

