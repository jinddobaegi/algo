import sys
sys.stdin = open('input.txt')

# dp[n][0] = (n을 루트로 하는 서브트리의 최대 독립집합 크기. n 포함 x)
# dp[n][1] = (n을 루트로 하는 서브트리의 최대 독립집합 크기. n 포함 o)
#
# path[n][0] = (n을 루트로 하는 서브트리의 독립집합 원소. n 포함 x)
# path[n][1] = (n을 루트로 하는 서브트리의 독립집합 원소. n 포함 x)

# 독립집합 : 그래프에서 서로 인접하지 않은 노드들의 집합

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
path = [[[] for _ in range(2)] for _ in range(N+1)]
W = [0] + list(map(int, sys.stdin.readline().split()))
visit = [False] * (N+1)
# print(dp)
for _ in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)


def dfs(node):
    visit[node] = True
    dp[node][1] += W[node]
    path[node][1].append(node)

    for x in tree[node]:
        if not visit[x]:
            result = dfs(x)  # 각 자식노드에 재귀적으로 dfs호출해서 서브트리 탐색

            # 독립집합이니까 케이스를 나눠줘야함
            dp[node][0] += max(dp[x][0], dp[x][1]) # 현재 노드가 독립집합에 포함되지 않는 경우 자식 노드중 더 큰 값 선택
            dp[node][1] += dp[x][0] # 현재 노드가 독립집합에 포함되면 자식노드는 포함될 수 없으니까 dp[x][0] 을 선택

            path[node][1] += result[0]
            if dp[x][0] > dp[x][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]

    return path[node]


p = dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    p[0].sort()
    for i in p[0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    p[1].sort()
    for i in p[1]:
        print(i, end=' ')