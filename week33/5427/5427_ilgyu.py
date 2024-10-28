import sys
input = sys.stdin.readline
from collections import deque

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def sol():
    while q:
        info, x, y, cnt = q.popleft()
        # 여기서 x, y가 불인지 상근인지 구분 어떻게 ?
        # 여기서 분기처리
        if info == "fire":
        # 불 확산
            for k in range(4):
                nx, ny = x + di[k], y + dj[k]
                if 0 <= nx < h and 0 <= ny < w and area[nx][ny] == ".":
                    q.append(["fire", nx, ny, cnt + 1])
                    area[nx][ny] = "*"
        # 상근이 이동
        elif info == "sang":
            # 탈출 성공
            if x == 0 or x == h-1 or y == 0 or y == w-1:
                return cnt + 1

            for k in range(4):
                nx, ny = x + di[k], y + dj[k]
                if 0 <= nx < h and 0 <= ny < w and area[nx][ny] == ".":
                    q.append(["sang", nx, ny, cnt + 1])
                    area[nx][ny] = "@"

    return "IMPOSSIBLE"


T = int(input())
for tc in range(1, T+1):
    w, h = map(int, input().split())
    area = [list(map(str, input())) for _ in range(h)]

    # * 불이 여러 개일 수도 있음 => 불위치 찾아서 동시에 확산
    # 1. 불위치 정보
    q = deque()
    for i in range(h):
        for j in range(w):
            if area[i][j] == "*":
                q.append(["fire", i, j, 0])
    # print(fire)
    # 2. 상근이 위치
    for i in range(h):
        for j in range(w):
            if area[i][j] == "@":
                q.append(["sang", i, j, 0])

    print(sol())
    # q에 불위치 다담고 상근이 위치 담고 while돌리면 알아서 불 => 상근이 순서로 이동


