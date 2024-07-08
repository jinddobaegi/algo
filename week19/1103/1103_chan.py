import sys
sys.stdin = open("week19/1103/1103.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 형택이는 1부터 9까지의 숫자와, 구멍이 있는 직사각형 보드에서 재밌는 게임을 한다.

# 일단 보드의 가장 왼쪽 위에 동전을 하나 올려놓는다. 그 다음에 다음과 같이 동전을 움직인다.

# 1. 동전이 있는곳에 쓰여 있는 숫자 x를 본다.
# 2. 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
# 3. 동전을 위에서 고른 방향으로 x만큼 움직인다. 이때 중간에 있는 구멍은 무시한다.

# 만약 동전이 구멍에 빠지거나 , 보드의 바깥으로 나간다면 게임은 종료된다. 형택이는 이 재밌는 게임을 되도록이면 오래 하고 싶다.
# 보드의 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 잇는지 구하는 프로그램을 작성하시오

# def move(x, y, count):
#     global max_move
#     if board[x][y] == IndexError or board[x][y] == "H":
#         max_move = max(max_move, count)
#         return
    
#     for dx, dy in delta:
#         nx, ny = x + (dx * board[x][y]), y + (dy * board[x][y])
#         if 0<= nx < N and 0 <= ny < M:
#             move(nx, ny, count + board[x][y])
            

# move(0, 0, 0)

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_board(x, y):
    return 0 <= x < N and 0 <= y < M

def dfs(x, y):
    if not in_board(x, y) or board[x][y] == 'H':
        return 0
    elif dp[x][y] != -1:
        return dp[x][y]
    elif visited[x][y]:
        return float('inf')  # 무한 루프가 발생한 경우 매우 큰 값을 반환하여 처리

    visited[x][y] = True
    move_distance = int(board[x][y])
    max_moves = 0

    for dx, dy in directions:
        nx, ny = x + dx * move_distance, y + dy * move_distance
        max_moves = max(max_moves, dfs(nx, ny) + 1)
    
    visited[x][y] = False
    dp[x][y] = max_moves
    return dp[x][y]

result = dfs(0, 0)
print(-1 if result == float('inf') else result)