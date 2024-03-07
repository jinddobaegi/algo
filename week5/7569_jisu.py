# 토마토

M, N, H = map(int, input().split()) # 가로: M, 세로: N, 높이: H
box = [] # [1번박스:[[한줄],[두줄]], 2번박스:[[한줄],[두줄]]]
cnt = 0
place = [] # 탐색하면서 1 있는 위치 저장

for i in range(H):
    a = []
    for j in range(N):
        a.append(list(map(int, input().split())))
        cnt += a[j].count(-1)
        cnt += a[j].count(1)
    box.append(a)

if M * N * H == cnt:
    print(0)
else:
    3