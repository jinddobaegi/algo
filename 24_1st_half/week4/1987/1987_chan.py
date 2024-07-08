import sys
sys.stdin = open('1987.txt')

# 왜 틀리는지... 알 수 가 없음 => 다시 새롭게 해보려함
# def DFS(r, c):
#     if graph[r][c] not in checklist and visited[r][c] == 0:
#         checklist.append(graph[r][c])
#         visited[r][c] = 1
#         delta = [[0,1],[0,-1],[1,0],[-1,0]]
#         for i in delta:
#             nr = r + i[0]
#             nc = c + i[1]
#             if 0 <= nr < sero and 0 <= nc < garo:
#                 if visited[nr][nc] == 0:
#                     DFS(nr,nc)

# sero, garo = map(int, input().split())
# visited = [[0]*garo for _ in range(sero)]
# checklist = []
# graph = []
# count = 0
# for _ in range(sero):
#     graph.append(input())

# DFS(0,0)
# print(len(checklist))




# 시간초과
# def dfs(r, c, count):
#     global max_count

#     visited.add(graph[r][c])
#     max_count = max(max_count, count)

#     for a, b in [(0,1),(0,-1),(1,0),(-1,0)]:
#         nr, nc= r+a, c+b
#         if 0 <= nr < row and 0 <= nc < col and graph[nr][nc] not in visited:
#             dfs(nr, nc, count + 1)
#     visited.remove(graph[r][c])



# row, col = map(int, input().split())
# graph = [list(input()) for _ in range(row)]
# visited = set()

# max_count = 0

# dfs(0, 0, 1)

# print(max_count)


def dfs(r, c, count):
    global max_count
    max_count = max(max_count, count)

    for a, b in [(0,1),(0,-1),(1,0),(-1,0)]:
        nr, nc= r+a, c+b
        if 0 <= nr < row and 0 <= nc < col and not visited[ord(graph[nr][nc]) - ord("A")]:
            visited[ord(graph[nr][nc]) - ord("A")] = True
            dfs(nr, nc, count + 1)
            visited[ord(graph[nr][nc]) - ord("A")] = False
            

row, col = map(int, input().split())
graph = [list(input()) for _ in range(row)]
visited = [False] * 26

max_count = 0

visited[ord(graph[0][0]) - ord("A")] = True
dfs(0, 0, 1)

print(max_count)



