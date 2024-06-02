import sys
sys.stdin = open("week15/14500/14500.txt")
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

# ㅗ, ㅏ, ㅓ, ㅜ 모양의 테트로미노를 따로 처리하는 함수
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

def tetris(x, y):
    global max_sum
    max_num = 0
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    queue.append((x, y, 1, graph[x][y]))
    
    while queue:
        x, y, count, num = queue.popleft()
        if count == 4:
            max_num = max(max_num, num)
            continue
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                queue.append((nx, ny, count + 1, num + graph[nx][ny]))
    
    check_t_result = check_t(x, y)
    max_sum = max(max_sum, max_num, check_t_result)

for row in range(N):
    for col in range(M):
        tetris(row, col)

print(max_sum)

