import sys
sys.stdin = open('input.txt')
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def sol(a1, b1, a2, b2):
    q = deque()
    q.append([a1, b1, a2, b2, 0])

    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if cnt >= 10: # 여기서 크거나 같은 이유가 어차피 return 할 때 +1 되니까
            return -1

        for k in range(4):
            nx1, ny1 = x1 + di[k], y1 + dj[k]
            nx2, ny2 = x2 + di[k], y2 + dj[k]

            # 둘 다 안떨어짐
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if board[nx1][ny1] == "#": # 동전1이 벽에 막힘
                    nx1, ny1 = x1, y1 # 원위치
                if board[nx2][ny2] == "#": # 동전2 벽에 막힘
                    nx2, ny2 = x2, y2
                # 겹칠 수 이씅니까 if로
                q.append([nx1, ny1, nx2, ny2, cnt + 1])

            # 동전1 떨어짐
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
            # 동전2 떨어짐
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1
            # 둘 다 떨어짐
            else:
                continue
    # while이 다 끝나면 둘 다 떨어지는 경우만 있었다는 뜻
    return -1


n, m = map(int, input().split()) # 세로, 가로
board = [list(map(str, input())) for _ in range(n)]

start = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            start.append([i, j])
# print(start)
x1, y1, x2, y2 = start[0][0], start[0][1], start[1][0], start[1][1]
ans = sol(x1, y1, x2, y2)
print(ans)

