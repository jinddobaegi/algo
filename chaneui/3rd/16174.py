import sys
sys.stdin = open("16174.txt")

size = int(input())
visited = [[0]*size for _ in range(size)]
board = [list(map(int, input().split())) for _ in range(size)]

def DFS(row, col):
    if row >= size or col >= size or visited[row][col] == 1:
        return False
    if board[row][col] == -1:
        return True

    visited[row][col] = 1
    position = board[row][col]

    return DFS(row+position, col) or DFS(row, col+position)

if DFS(0,0):
    print("HaruHaru")
else:
    print("Hing")
