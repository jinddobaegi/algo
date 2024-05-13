# 특정 거리의 도시 찾기
# 트리
# 단방향?
# BFS로 가장 인접한 노드들 다 접근해서 cnt += 1 해준 후
# cnt == K가 되면 멈추고
# 다 돌았는데 cnt < K 면 -1
# visited를 이용해서 부모노드에 재 방문 안되게.
# from collections import deque

# # N: 도시(노드), M: 도로(간선), K: 거리, X: 출발도시(루트)
# N, M, K, X = map(int, input().split())
# visited = [[] * (N + 1)]
# parent = [[] * (N + 1) for _ in range(N + 1)]
# q = deque()

# for i in range(M):
#     a, b = map(int, input().split())
#     parent[a].append(b)

# # [[], [2, 3], [3, 4], [], []]
# def bfs(X):
#     q.append(X)
#     visited[X] = 1
#     while q:
#         x = q.popleft()

from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)