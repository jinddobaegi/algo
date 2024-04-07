import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, w = map(int, input().split())  # 부모, 자식, 가중치
    arr[p].append([c, w])
    arr[c].append([p, w])

def dfs(s, dis):
    for ch, ch_d in arr[s]:
        if visited[ch] == -1:
            visited[ch] = dis + ch_d   # 이전 노드 가중치 + 현재 노드 가중치
            dfs(ch, dis + ch_d)

# 루트에서 가장 먼 노드 찾기
visited = [0] * (N+1)
visited[1] = 0    # 가중치 0으로 초기화
dfs(1, 0)

# 찾은 노드에서 가장 먼 노드 찾아서 dfs 탐색
last_w = visited.index(max(visited))
visited = [-1] * (N+1)
visited[last_w] = 0
dfs(last_w, 0)

print(max(visited))




# for _ in range(N-1):
#     p, c, w = map(int, input().split())  # 부모, 자식, 가중치
#     arr[p].append([c, w])
#     arr[c].append([p, w])
#
# def dfs(s, dis):
#     for ch, ch_d in arr[s]:
#         if visited[ch] == 0:
#             visited[ch] = dis + ch_d   # 이전 노드 가중치 + 현재 노드 가중치
#             dfs(ch, dis + ch_d)
#
# # 루트에서 가장 먼 노드 찾기
# visited[1] = 0    # 가중치 0으로 초기화
# dfs(1, 0)
#
# # 찾은 노드에서 가장 먼 노드 찾기
# last_w = visited.index(max(visited))
# visited = [0] * (N+1)
# visited[last_w] = 0
# dfs(last_w, 0)
#
# print(max(visited))