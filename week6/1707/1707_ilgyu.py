import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(start, graph, color):
    q = deque()
    q.append(start)
    color[start] = 0  # 시작점을 파랑(0)으로 칠하고 시작

    while q:
        s = q.popleft()
        for node in graph[s]:
            if color[node] == -1:  # 아직 색이 안 칠해져 있으면 s와 반대색으로 색칠
                color[node] = 1 - color[s]
                q.append(node)
            elif color[node] == color[s]:  # 인접한 노드가 같은 색인 경우
                return False  # 이분 그래프가 아님
    return True  # 모든 검사를 통과함, 이분 그래프임

# 입력 처리 방식 개선
# input = sys.stdin.readline  # 빠른 입력 처리를 위해 sys.stdin.readline 사용
# 이거 쓰면 되고 안쓰면 안됨 뭐지

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    color = [-1] * (V + 1)  # 이분그래프 판별용 + 방문여부

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    is_bipartite = True
    for i in range(1, V + 1):
        if color[i] == -1:
            if not bfs(i, graph, color):
                is_bipartite = False
                break

    print('YES' if is_bipartite else 'NO')
