import sys
sys.stdin = open("week15/14502/14502.txt")
input = sys.stdin.readline
from collections import deque
from itertools import combinations


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def bfs(): # 바이러스의
    queue = deque()
    temp_graph = [row[:] for row in graph]  # 임시 그래프 사용
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 2: # 바이러스가 있으면 
                queue.append((i, j)) # queue에 넣는다.
    
    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    while queue: # 전염시키기
        x, y = queue.popleft() 
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2
                queue.append((nx, ny))
    
    count = 0 #0의 개수 구하기
    for i in range(N):
        for j in range(M):
            if temp_graph[i][j] == 0:
                count += 1
    return count

def set_walls_and_calculate(): # 벽을 만들고 0을 계산
    max_safe_area = 0 # 안전지역 초기화
    empty_spaces = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 0] # 0인 것만
    # print(empty_spaces)
    for walls in combinations(empty_spaces, 3): # 점이 0인 것들 중에서 3개에 벽을 세운다
        for x, y in walls:
            graph[x][y] = 1
        max_safe_area = max(max_safe_area, bfs()) #0 의 객수가 많은 것을 구한다.
        for x, y in walls: # 다시 초기화 한다.
            graph[x][y] = 0
    return max_safe_area # 안전지역을 리턴

print(set_walls_and_calculate())
