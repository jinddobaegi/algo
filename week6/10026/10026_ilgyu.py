import sys
sys.stdin = open('input.txt')
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 일반 사람용 함수
def count_area_normal(i, j):
    q = deque()
    start = [i, j]
    q.append(start)
    visited_N[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < N and 0 <= ny < N and visited_N[nx][ny] == False and drawing[x][y] == drawing[nx][ny]:
                visited_N[nx][ny] = True
                q.append([nx, ny])

# 적록색약용 함수
def count_area_blind(i, j):
    q = deque()
    start = [i, j]
    q.append(start)
    visited_B[i][j] = True

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + di[k], y + dj[k]
            if 0 <= nx < N and 0 <= ny < N and visited_B[nx][ny] == False: # 범위안에 있고 방문한적 없으면
                if drawing[x][y] == 'R' or drawing[x][y] == 'G': # 빨강, 초록인 경우에
                    if drawing[nx][ny] == 'R' or drawing[nx][ny] == 'G': # 다음애도 빨강, 초록이면 같은 색으로 보니까
                        visited_B[nx][ny] = True
                        q.append([nx, ny])
                elif drawing[x][y] == 'B' and drawing[nx][ny] == 'B': # 파랑의 경우 그냥 else: 이렇게 처리할게아니라
                                                                      # 다음것도 파랑인경우로 지정해줘야해
                    visited_B[nx][ny] = True
                    q.append([nx, ny])


N = int(input())
drawing = [list(map(str, input())) for _ in range(N)]
visited_N = [[False] * N for _ in range(N)] # 일반용
visited_B = [[False] * N for _ in range(N)] # 적록색약
# print(drawing)
# print(visited)

normal = 0 # 일반사람
blind = 0 # 적록색약

# 일반사람용 검사
for i in range(N):
    for j in range(N):
        if visited_N[i][j] == False:
            count_area_normal(i, j)
            normal += 1

# 적록색약용 검사
for i in range(N):
    for j in range(N):
        if visited_B[i][j] == False:
            count_area_blind(i, j)
            blind += 1

print(normal, end=" ")
print(blind)
