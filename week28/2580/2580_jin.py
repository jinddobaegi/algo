from sys import stdin

input = stdin.readline

def check_row(r, num):
    return not (num in arr[r])


def check_col(c, num):
    for r in range(9):
        if arr[r][c] == num:
            return False
    return True


def check_square(r, c, num):
    r = (r//3)*3
    c = (c//3)*3
    for i in range(r, r+3):
        for j in range(c, c+3):
            if arr[i][j] == num:
                return False
    return True


def sudoku(z_idx):
    if z_idx == cnt:
        for line in arr:
            print(*line)
        exit()
        # return True  # exit() 쓰기 싫어서 찾아본 방법인데 시간이 2000ms정도 더 걸린다

    for num in range(1, 10):
        r, c = zeros[z_idx]
        if check_row(r, num) and check_col(c, num) and check_square(r, c, num):
            arr[r][c] = num
            sudoku(z_idx+1)
            # if sudoku(z_idx+1):
            #     return
            arr[r][c] = 0


arr = list(list(map(int, input().split())) for _ in range(9))
zeros = []  # 빈칸의 좌표
cnt = 0  # 빈칸의 개수
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zeros.append((i, j))
            cnt += 1

sudoku(0)