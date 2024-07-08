import sys
sys.stdin = open('input.txt')

def dfs(s, first):
    global total
    global ans

    if len(res) == n:
        last_city = res[-1]
        if costs[last_city][first] != 0: # 마지막도시에서 시작도시로 길이 있으면
            total += costs[last_city][first] # 마지막 도시에서 시작점으로 가는 비용
            ans = min(ans, total)
            total -= costs[last_city][first]
        return
    # 0-1-2-3 순서로 방문시
    # dfs(0, 0)부터 시작해서 dfs(3, 0)이 마지막 재귀함수가 되는데
    # dfs(3, 0)에서 len(res) == 4가 됨 => 여기서 ans값 갱신

    for next, cost in graph[s]:
        if not visited[next]:
            visited[next] = True
            res.append(next)
            total += cost
            dfs(next, first)
            visited[next] = False
            res.pop()
            total -= cost


n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
# print(cost)

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and costs[i][j] != 0: #
            target, cost = j, costs[i][j]
            graph[i].append([target, cost])

ans = float('inf')
for m in range(n): # 0~3까지 모두 시작점으로 놔보기
    visited = [False] * n
    visited[m] = True
    res = []
    res.append(m)
    total = 0 # m을 시작으로 놨을 때 총 비용
    dfs(m, m)
# for m in graph:
#     print(m)
print(ans)

# 10줄이랑 34줄에 costs[i][j] != 0 인 경우를 조건으로 안 걸어주면 답이 틀리게 나옴
# 왜냐하면 모든 도시를 순회한 조건을 res안에 도시를 담는 식으로 했는데
# 단순히 res의 길이가 n이라고 해서 마지막 도시에서 시작 도시까지 길이 있을 거라는 보장이 없음
# 0-1-2-3 순서로 갈 수 있더라도 3 -> 0으로 가는 길이 없으면 이 경우는 제외시켜야함
