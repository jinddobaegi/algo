# 부분 집합 구해서 인접 확인을 해야하나..? -> X
# dp 활용

N = int(input())  # 트리의 정점 수
w = list(map(int, input().split()))
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
DP = [[0,0] for _ in range(N+1)]  # 해당 노드 선택한 경우 / 선택하지 않은 경우

for _ in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(node):
    visited[node] = 1
    DP[node][0] = w[node]

    for i in tree[node]:
        if visited[i] == 0:
            dfs(i)
            # 아직 풀어보는 중

dfs(1)