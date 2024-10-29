import sys
sys.stdin = open("week33/5427/5427.txt")
from collections import deque

# 불 이동 -> 1턴에 동서남북으로 퍼져나감
# 상근 이동 -> 동서남북중에 이동
# 가장 빨리 나가는 경우 찾기
# 못나가면 임파서블


# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불

# 방향 설정 (상, 하, 좌, 우)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(W, H, building, fire_queue, escape_queue):
    while escape_queue:
        # 불 이동
        fire_size = len(fire_queue)
        for _ in range(fire_size):
            r, c = fire_queue.popleft()
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W and building[nr][nc] == '.':
                    building[nr][nc] = '*'
                    fire_queue.append((nr, nc))

        # 상근이 이동
        escape_size = len(escape_queue)
        for _ in range(escape_size):
            r, c, sec = escape_queue.popleft()
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                # 건물 밖으로 나가는 경우
                if not (0 <= nr < H and 0 <= nc < W):
                    return sec + 1
                if building[nr][nc] == '.':
                    building[nr][nc] = '@'
                    escape_queue.append((nr, nc, sec + 1))
    
    return "IMPOSSIBLE"

T = int(input())

for _ in range(T):
    W, H = map(int, input().split())
    building = [list(input().strip()) for _ in range(H)]

    fire_queue = deque()
    escape_queue = deque()

    for i in range(H):
        for j in range(W):
            if building[i][j] == '*':
                fire_queue.append((i, j))
            elif building[i][j] == '@':
                escape_queue.append((i, j, 0))  

    result = bfs(W, H, building, fire_queue, escape_queue)
    print(result)