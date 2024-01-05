# bfs
# 인접한 모든 정점을 방문 후
# 각 인접 정점의 인접 정점을 방문
# 위 과정을 반복하며, 모든 방문 가능한 정점을 방문

# 코드로 짜면
# 큐에 시작 정점 enqueue
# 큐에서 하나씩 dequeue하며 반환되는 정점과 인접한 정점을 큐에 삽입
# 반복하다가 큐가 비면 탐색 종료

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

from collections import deque

def bfs(s, V):
    visited = [0] * (V+1)
    dq = deque()
    dq.append(s)
    visited[s] = 1
    while dq:
        v = dq.popleft()
        print(v)
        for w in adj_list[v]:
            if visited[w] == 0:
                dq.append(w)
                visited[w] = visited[v] + 1
    # print(visited)

bfs(1, 7)

