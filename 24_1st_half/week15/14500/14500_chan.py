import sys
sys.stdin = open("week15/14500/14500.txt")
input = sys.stdin.readline
from collections import deque

# N, M = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# max_sum = 0

# # ㅗ, ㅏ, ㅓ, ㅜ 모양의 테트로미노를 따로 처리하는 함수
# def check_t(x, y):
#     t_shapes = [
#         # ㅗ 모양
#         [(0, 0), (-1, 0), (0, -1), (0, 1)],
#         # ㅜ 모양
#         [(0, 0), (1, 0), (0, -1), (0, 1)],
#         # ㅏ 모양
#         [(0, 0), (0, 1), (-1, 0), (1, 0)],
#         # ㅓ 모양
#         [(0, 0), (0, -1), (-1, 0), (1, 0)]
#     ]
    
#     max_t = 0
#     for shape in t_shapes:
#         try:
#             temp_sum = sum(graph[x + dx][y + dy] for dx, dy in shape)
#             max_t = max(max_t, temp_sum)
#         except IndexError: #에러나면 다음꺼해
#             continue
    
#     return max_t

# def tetris(x, y):
#     global max_sum
#     max_num = 0
#     delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque()
#     queue.append((x, y, 1, graph[x][y]))
    
#     while queue:
#         x, y, count, num = queue.popleft()
#         if count == 4:
#             max_num = max(max_num, num)
#             continue
#         for dx, dy in delta:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < M:
#                 queue.append((nx, ny, count + 1, num + graph[nx][ny]))
    
#     check_t_result = check_t(x, y)
#     max_sum = max(max_sum, max_num, check_t_result)

# for row in range(N):
#     for col in range(M):
#         tetris(row, col)

# print(max_sum)



#두번쨰
# 테트리스 
# 테트리스는 4개의 정사각형을 붙인것이고 5개로 이루어져있다.
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

def check_t(x, y):
    t_shapes = [
        # ㅗ 모양
        [(0, 0), (-1, 0), (0, -1), (0, 1)],
        # ㅜ 모양
        [(0, 0), (1, 0), (0, -1), (0, 1)],
        # ㅏ 모양
        [(0, 0), (0, 1), (-1, 0), (1, 0)],
        # ㅓ 모양
        [(0, 0), (0, -1), (-1, 0), (1, 0)]
    ]
    
    max_t = 0
    for shape in t_shapes:
        try:
            temp_sum = sum(graph[x + dx][y + dy] for dx, dy in shape)
            max_t = max(max_t, temp_sum)
        except IndexError: #에러나면 다음꺼해
            continue
    
    return max_t


def check(x, y, count, tetris_sum):
    global max_sum
    if count == 3:
        max_sum = max(max_sum, tetris_sum)
        return
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < row and 0 <= ny < col:
            check(nx, ny, count + 1, tetris_sum + graph[nx][ny])

def check_tetris(x, y):
    global max_sum
    check(x, y, 1, graph[x][y])
    check_t_result = check_t(x, y)
    max_sum = max(max_sum, check_t_result)



max_sum = 0
row, col = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(row)]

# for i in graph:
#     print(i)

# 테트리스를 하나를 놓았을때 최대의 값을 구해야한다.

for i in range(row):
    for j in range(col):
        check_tetris(i, j)

print(max_sum)

