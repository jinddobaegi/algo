# 그냥 했다가 런타임 에러 나서
# sys.setrecursionlimit(10**6) 추가했는데 시간 초과 뜸 ㅠㅠ
# 아래처럼 설정해주니까 통과했음...
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = 0

def dfs(s):
    visited[s] = 1

    for i in arr[s]:
        if visited[i] == 0:
            dfs(i)

for _ in range(M):
    U, V = map(int, input().split())
    arr[U].append(V)
    arr[V].append(U)

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        ans += 1

print(ans)