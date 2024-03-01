import sys
sys.stdin = open("1012.txt")

def DFS(r, c):
    visited[r][c] = 1
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in delta:
            nr = r + i[0]
            nc = c + i[1]
            if 0<=nr<row and 0<=nc<col:
                if ground[nr][nc] == 1 and visited[nr][nc] == 0:
                    DFS(nr, nc)

T = int(input())
for _ in range(T):
    row, col, count = map(int, input().split())
    ground = [[0]*col for _ in range(row)]
    visited = [[0]*col for _ in range(row)]
    for _ in range(count):
        a, b = map(int, input().split())
        ground[a][b] += 1


    count = 0
    for r in range(row):
        for c in range(col):
            if ground[r][c] == 1 and visited[r][c] == 0:
                DFS(r, c)
                count += 1

    print(count)