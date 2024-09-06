import sys
sys.stdin = open("week28/16234/16234.txt")
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6) 

N,L,R = map(int, input().split())

population = [list(map(int, input().split()))for _ in range(N)]    

# print(population)

union_day = 0

def cal(change_set):
    leg_set = len(change_set)
    queue = deque(change_set)
    alpa = 0
    while queue:
        a, b = queue.popleft()
        alpa += population[a][b]

    change_alpa = alpa // leg_set  # 평균 인구 수 계산
    
    for a, b in change_set:  # 모든 위치에 대해 평균 인구 수를 설정
        population[a][b] = change_alpa

def bfs(i, j, visited):
    queue = deque([(i, j)])
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    change_set = set()
    while queue:
        r, c = queue.popleft()

        for a, b in delta:
            nr, nc = r + a, c + b
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if L <= abs(population[r][c] - population[nr][nc]) <= R:
                    visited[nr][nc] = True
                    change_set.add((nr, nc))
                    queue.append((nr, nc))
    return change_set
    

def find_root():
    global union_day
    visited = [[False]*N for _ in range(N)]
    flage = False
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                change_set = bfs(i, j, visited)
                if len(change_set) > 1:
                    cal(change_set)
                    flage = True

    if flage:
        union_day += 1
        find_root()
    else:
        return

find_root()
print(union_day)
    

