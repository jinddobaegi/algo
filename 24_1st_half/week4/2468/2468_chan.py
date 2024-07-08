import sys
sys.stdin = open("2468.txt")

# N = int(input())

# def dfs(r,c,rain,city):
#     global max_city
#     max_city = max(max_city, city)
#     for a in range(N):
#         for b in range(N):
#             if graph[a][b] <= rain:
#                 visited[a][b] = 1
    
#     delta = [(0,1), (0,-1), (1,0), (-1,0)]
#     for a, b in delta:
#         nr, nc = r + a, c + b
#         if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] != 1:
#             dfs(nr, nc,rain-1,city+1)


# graph =[list(map(int, input().split())) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]

# max_num = 0
# max_city = 0
# for i in range(N):
#     if max_num < max(graph[i]):
#         max_num = max(graph[i])

# dfs(0,0,max_num-1, 0)

# print(max_city)

def dfs(row,col,city,max_num):
    global max_city
    max_city = max(max_city, city)

    for r in range(N):
        for c in range(N):
            if graph[r][c] <= max_num:
                visited[r][c] = 2
    


N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
max_city = 0
max_num = 0
for i in graph:
    if max_num < max(i):
        max_num = max(i)

dfs(0,0,0,max_num)