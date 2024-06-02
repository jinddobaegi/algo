import sys
sys.stdin = open("week15/14502/14502.txt")
input = sys.stdin.readline
from collections import deque
from itertools import combinations


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 원래 그래프를 유지하기 위해 복사
original_graph = [row[:] for row in graph]

def bfs():
    queue = deque()
    temp_graph = [row[:] for row in graph]  # 임시 그래프 사용
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2:
                queue.append((i, j))
    
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                count += 1
    return count

def set_walls_and_calculate():
    max_safe_area = 0
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 0]
    for walls in combinations(empty_spaces, 3):
        for x, y in walls:
            graph[x][y] = 1
        max_safe_area = max(max_safe_area, bfs())
        for x, y in walls:
            graph[x][y] = 0
    return max_safe_area

print(set_walls_and_calculate())
