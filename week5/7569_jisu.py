# 토마토
from collections import deque

def bfs():
    global cnt
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dk[i]
            nx = x + di[i]
            ny = y + dj[i]

            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0:
                q.append((nz, nx, ny))
                # 토마토를 익힐때마다 하루씩 걸리니까
                # 그 전의 토마토 데이(?)에 하루 더 더해주기
                # 이거로 날짜구해야지
                box[nz][nx][ny] = box[z][x][y] + 1

                if cnt < box[nz][nx][ny]:
                    cnt = box[nz][nx][ny]

M, N, H = map(int, input().split()) # 가로: M, 세로: N, 높이: H
box = [] # [1번박스:[[한줄],[두줄]], 2번박스:[[한줄],[두줄]]]
cnt = 1 # 하루부터 시작
# place = [] # 탐색하면서 1 있는 위치 저장 # 아 dfs 안될꺼같아(해보진 않음)
q = deque()

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

# 박스 속 토마토 구현
# 이긴한데 그냥 여기서 할 수 있는건 여기서 다 받아버리기~!
for k in range(H):
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
        # cnt += a[j].count(-1)
        # cnt += a[j].count(1)
        for j in range(M): # a가 한 층 네모니까
            if a[i][j] == 1:
                q.append([k, i, j])
    box.append(a)

#bfs 사용하겠어
bfs()

for k in range(H):
    for i in range(N):
        if 0 in box[k][i]:
            print(-1)
            # break는 for문 하나만 종료함. 그냥 완전 끝내려면 exit()
            exit()
    if k == H - 1:
        print(cnt - 1) # cnt가 1에서 시작하니까! 이렇게 하면 토마토 다 익었을 때도 0 print 할 수 있음!!!





# 이딴게 알고리즘? ㅠ
# if M * N * H == cnt:
#     print(0)
# else: