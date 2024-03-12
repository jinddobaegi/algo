import sys
sys.stdin = open('input.txt')
from collections import deque

M, N, H = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N*H)]
visited = [[False] * M for _ in range(N*H)]
# print(boxes)
di = [0, 1, 0, -1, N, -N]
dj = [1, 0, -1, 0, 0, 0]

def check_all_ripe(boxes):
    for row in boxes:
        if 0 in row:  # 익지 않은 토마토가 있는 경우
            return False
    return True

# 다른층의 토마토를 검사할 때?
# 애초에 내가 리스트를 그냥 2차원으로 쭉 만들엇으니까
# 윗층박스의 토마토는 i, j 기준으로 i + N
def find_ripe(start):
    q = start
    total = 0
    while q:
        x, y, day = q.popleft()
        visited[x][y] = True

        floor = x//N

        total = day
        for k in range(6):
            nx, ny = x + di[k], y + dj[k]
            if (0 <= nx < N * H and 0 <= ny < M):
                if (boxes[nx][ny] == 0 and nx // N == floor):
                    visited[nx][ny] = True
                    boxes[nx][ny] = 1
                    q.append([nx, ny, day + 1])

                     # 0 0 0 0
                     # 0 0 0 0
                     # 0 0 0 0
                     # 0 0 1 0
                     # 0 0 0 0
                     # 0 0 0 0 일때 1은 바로 윗줄의 0에는 영향을 주면 안됨

                elif (boxes[nx][ny] == 0):
                    if (k == 4 or k == 5):
                        visited[nx][ny] = True
                        boxes[nx][ny] = 1
                        q.append([nx, ny, day + 1])

    for i in range(N*H):
        if 0 in boxes[i]:
            return -1
    return total

if check_all_ripe(boxes):  # 모든 토마토가 이미 익었는지 먼저 확인
    ans = 0
else:
    start = deque()
    for i in range(N*H):
        for j in range(M):
            if boxes[i][j] == 1 and not visited[i][j]:
                start.append([i, j, 0])

    ans = find_ripe(start)
print(ans)
# for m in boxes:
#     print(m)
#
# for n in visited:
#     print(n)
