from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
order = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
arr = list(map(int, input().split()))

def bfs():
    visited = [0] * (N + 1)
    q = deque()
    q.append(1)
    visited[1] = 1
    lst = [1] # 방문 순서

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                lst.append(i)

    return lst

for i in range(N):
    order[arr[i]] = i

for i in range(1, N+1):  # 각 노드 인접 리스트 정렬
    graph[i].sort(key=lambda x:order[x])

lst = bfs()

# 두 리스트가 같다면 올바른 순서
if lst == arr:
    print(1)
else:
    print(0)