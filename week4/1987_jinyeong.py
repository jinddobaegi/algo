from sys import stdin
input = stdin.readline

R, C = map(int, input().split())

arr = list(list(input().strip()) for _ in range(R))
visited = list()
arr_visited = list([0]*C for _ in range(R))
visited.append(arr[0][0])
arr_visited[0][0] = 1

dr = [1,-1,0,0]
dc = [0,0,-1,1]


def bfs(r, c):
    global max_v
    global cnt

    cnt += 1
    if max_v < cnt:
        max_v = cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if (arr[nr][nc] not in visited) and (not arr_visited[nr][nc]):
                visited.append(arr[nr][nc])
                arr_visited[nr][nc] = 1
                bfs(nr, nc)
                visited.pop()
                arr_visited[nr][nc] = 0
                cnt -= 1


max_v = 0
cnt = 0

bfs(0,0)

print(max_v)