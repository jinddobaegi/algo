# pypy로 하기 싫었는데 흑흑
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
cnt = [0]
c_cnt = 1

def bfs(com):
    global c_cnt
    q = deque()
    q.append(com)
    visited = [0] * (N + 1)
    visited[com] = 1

    while q:
        c = q.popleft()
        for i in arr[c]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                c_cnt += 1
    return c_cnt

for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

for i in range(1, N+1):
    bfs(i)
    cnt.append(c_cnt)
    c_cnt = 1

max_com = []
for i in range(1, N+1):
    if cnt[i] == max(cnt):
        max_com.append(i)

print(*max_com)


# 처음에 dfs로 풀었으나 시간 초과ㅠㅠ
# def dfs(computer):
#     global c_cnt
#     for i in arr[computer]:
#         if visited[i] == 0:
#             visited[i] = 1
#             c_cnt += 1
#             dfs(i)