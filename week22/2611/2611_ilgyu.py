import sys
sys.stdin = open('input.txt')
from collections import deque

def sol(s):
    q = deque()
    q.append(s)

    while q:
        print(q)
        node = q.popleft()
        for next, weight in road[node]:
            indegree[next] -= 1 # 다음노드로 가면서 그 경로 삭제
            if dp[node][0] + weight > dp[next][0]: # dp값이 크면 갱신
                # indegree[next] -= 1
                dp[next][0] = dp[node][0] + weight
                dp[next][1] = dp[node][1] + [next]
                # print(dp[next])
            if indegree[next] == 0:
                q.append(next)


n = int(input())
m = int(input())
road = [[] for _ in range(n+1)]
indegree = [0] * (n+1) # 노드별 진입 차수

for _ in range(m):
    p, q, r = map(int, input().split())
    road[p].append([q, r])
    indegree[q] += 1


dp = [[0, []] for _ in range(n+1)] # dp값은  (점수, 경로)
dp[1][1] = [1] # 마지막에 1로 돌아와야하니까 1번 노드의 진입차수는 1
sol(1)

# print(dp[1][0])
# print(' '.join(map(str, dp[1][1])))

# 위상정렬 쓰는 이유 : 각 노드가 특정 선행조건을 가짐