import sys
sys.stdin = open('input.txt')

row, col = map(int, input().split())
floor = [list(input()) for _ in range(row)]
counted = [[0]*(col) for _ in range(row)]

cnt = 0
for i in range(row):
    for j in range(col):
        if counted[i][j] == 0:
            if floor[i][j] == "-":
                # 가로 방향으로 이어진 '-'을 카운트
                y = j
                while y+1 < col and floor[i][y+1] == "-" and counted[i][y+1] == 0:
                    counted[i][y+1] = 1
                    y += 1
                cnt += 1

            elif floor[i][j] == "|":
                # 세로 방향으로 이어진 'ㅣ'을 카운트
                x = i
                while x+1 < row and floor[x+1][j] == "|" and counted[x+1][j] == 0:
                    counted[x+1][j] = 1
                    x += 1
                cnt += 1


print(cnt)
