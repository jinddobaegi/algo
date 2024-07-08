# 트리의 부모 찾기
# 실버2

# 문제
# 루트 없는
from collections import deque
import sys

N = int(input())

# 방문 지점 체크
visited = [False] * (N+1)
# 출력할 예정인 부모 노드 값들을 담을 수 있는 빈 리스트
parent_node = [0] * (N+1)

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    # 이걸 grpah 이중 리스트에 각각에 해당하는 인덱스에 연결된 노드를 다 담아주기
    graph[a].append(b)
    graph[b].append(a)


# 부모 찾느거니까 BFS 할거임
def bfs(graph, v, visited):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                parent_node[i] = x
                q.append(i)
                visited[i] = True


bfs(graph, 1, visited)

for i in range(2, N+1):
    print(parent_node[i])


