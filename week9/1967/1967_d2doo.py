# 트리의 지름
# 긴거 찾는거니까 깊이 우선이어야 할듯?

import sys
sys.setrecursionlimit(10**8) # dfs니까 일단,,

def dfs(S, dist):
    for next_node, next_dist in tree[S]:
        if visited[next_node] == -1:
            visited[next_node] = dist + next_dist
            dfs(next_node, dist + next_dist)

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(n - 1):
    parent, child, dist = map(int, input().split())
    tree[parent].append((child, dist)) # 무방향이니까
    tree[child].append((parent, dist)) # 다 넣어줘야함

visited[1] = 0 # 루트노드는 1이니까
dfs(1, 0)

last = visited.index(max(visited)) # 제일 큰 애가 last
visited = [-1] * (n + 1) # 방문기록 초기화
visited[last] = 0 # 젤 큰 애 기준으로 젤 먼애
dfs(last, 0)

print(max(visited))

# 아니 이게 어케되누?
# python3 -> 36700kb 500ms
# pypy -> 메모리 초과