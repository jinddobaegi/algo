import sys
input = sys.stdin.readline

# 가로
def row(n, x):
    for i in range(9):
        if area[x][i] == n: # 가로줄에 n이 있으면
            return False
    return True

# 세로
def col(n, y):
    for i in range(9):
        if area[i][y] == n:
            return False
    return True

# 사각형
def rec(x, y, n):
    x = x//3 * 3 # 해당 x,y가 속하는 작은 사각형의 시작점 찾기
    y = y//3 * 3
    for i in range(3):
        for j in range(3):
            if area[x+i][y+j] == n:
                return False
    return True

def sol(cnt):
    if cnt == len(blank):
        for i in range(9):
            print(*area[i])
        exit() # 안끝내면 cnt값이 blank길이 넘어가서 인덱스에러

    # 빈칸 첫번째 좌표부터 검사시작
    x = blank[cnt][0]
    y = blank[cnt][1]

    # 1~9까지 가로, 세로, 네모 안에 해당 숫자(i)가 있는지 확인
    for i in range(1, 10):
        if row(i, x) and col(i, y) and rec(x, y, i):
            area[x][y] = i
            sol(cnt + 1)
            area[x][y] = 0
            # 0으로 되돌려주는 이유 ?
            # 얘를들어 area[x][y] 값을 i로 해놓고 재귀타고 들어가서 계산하다
            # 어느 시점에 값이 안맞으면 되돌아와서 다른값으로 바꾸기 위해서?

area = [list(map(int, input().split())) for _ in range(9)]

# for m in area:
#     print(m)
blank = []
for i in range(9):
    for j in range(9):
        if area[i][j] == 0:
            blank.append([i, j])

sol(0)
