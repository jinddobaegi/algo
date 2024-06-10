# 트리의 독립집합
# ㅡㅡ

def dynamic(node):
    visited[node] = 1
    dp[node][1] += n_value[node]
    path[node][1].append(node)

    for x in tree[node]:
        if not visited[x]:
            result = dynamic(x)
            # 이걸 왜 더해? 뭘 더하는거임?
            dp[node][0] += max(dp[x][0], dp[x][1])
            dp[node][1] += dp[x][0]

            path[node][1] += result[0]
            if dp[x][0] > dp[x][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]

    return path[node]

n = int(input())
n_value = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n-1): # 양방향
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0] for _ in range(n + 1)]
visited = [0] * (n + 1)
path = [[[] for _ in range(2)] for _ in range(n + 1)]
'''
dp[n][0] = (n을 루트로 하는 서브트리의 최대 독립집합 크기. n 포함 x)
dp[n][1] = (n을 루트로 하는 서브트리의 최대 독립집합 크기. n 포함 o)

path[n][0] = (n을 루트로 하는 서브트리의 독립집합 원소. n 포함 x)
path[n][1] = (n을 루트로 하는 서브트리의 독립집합 원소. n 포함 x)
애초에 이걸 왜 하는지도 모르겠음
'''

ans = dynamic(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    ans[0].sort()
    for i in ans[0]:
        print(i, end=' ')
else:
    print(dp[1][1])
    ans[1].sort()
    for i in ans[1]:
        print(i, end=' ')

