N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

# 트리 만들기
for _ in range(N-1):
    n1, n2 = map(int, input().split())

    arr[n1].append(n2)
    arr[n2].append(n1)

# [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]
# 루트 1을 시작으로 타고타고 들어감
def dfs(s):
    for i in arr[s]:
        if visited[i] == 0:
            visited[i] = s   # visited에 1 대신 부모 노드 저장
            dfs(i)

dfs(1)

for i in range(2, N+1):
    print(visited[i])