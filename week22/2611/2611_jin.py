from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)


def dfs(v, visited, route, score):
    global max_score, res

    # Init
    if v == 1 and visited[v] == -1:
        visited[v] += 1
        route = [1]
    
    # 종료 조건
    if v == 1 and visited[v] == 1:
        # print('1 두 번째 방문')
        max_score = max(score, max_score)
        res = route
        return

    # 진행
    for w, r in adj_list[v]:
        if visited[w] <= 0:  # line 28 참고
            # print(f'{v}에서 {w}로!')
            visited[w] += 1  # 1은 두 번 가능
            dfs(w, visited, route + [w], score + r)
            visited[w] -= 1


N = int(input())
M = int(input())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    adj_list[p].append((q, r))

# 1번 노드로 돌아오는 것을 고려하여 1번 인덱스 -1로 설정
visited = [0] * (N+1)
visited[1] = -1
max_score = 0
res = []
dfs(1, visited, [], 0)

print(max_score)
print(*res)