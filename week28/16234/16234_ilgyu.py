import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def sol(i, j):
    q = deque()
    q.append([i, j])

    union = [[i, j]]
    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                dif = abs(area[x][y] - area[nx][ny])
                if L <= dif and dif <= R and [nx, ny] not in union:
                    union.append([nx, ny])
                    q.append([nx, ny])
    # 여기까지 하면 연합할 애들의 x,y 좌표가 union에 다 들어감
    if len(union) == 1:
        return False
    else:
        u_sum = 0
        for a, b in union:
            u_sum += area[a][b]

        res = u_sum // len(union)

        for a, b in union:
            area[a][b] = res

        return True


N, L, R = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if sol(i, j):
                    flag = True

    if not flag: # 인구이동 없으면 여기서 끊겨서 cnt 추가 x, while문 끝
        break

    cnt += 1


# for m in area:
#     print(m)
print(cnt)

# 2 20 50
# 50 30
# 40 20
# 위아래 반갈case, 1나와야함




# 1. 완탐후 열지 닫을지 결정
# 2. 인접한 두 나라가 국경을 열었는지 판단을 어떻게 할지
# 3. 단순히 True, False로 하기에는 오른쪽 국가랑은 열었는데, 아래쪽 국가랑은 닫는 경우도 있음
# 3. 또 옆 국가가 나랑은 국경을 닫았지만 결과적으로 연합에 같이 들어가는 경우도 있음
