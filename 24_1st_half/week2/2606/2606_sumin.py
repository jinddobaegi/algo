# 바이러스
# 실버 3
# DFS

import sys
N = int(input())
V = int(input())

# 방문할 노드 체크할 리스트
visited = [0]*(N+1)

# input 받을 공간
graph = [[] for _ in range(N+1)]
for _ in range(V):
    # map 이용해서 input 받는 것 
    com1, com2 = map(int, input().split())
    # 1->2 , 2->1 방향 다 있으니까 그거 다 저장하기
    graph[com1] += [com2]
    graph[com2] += [com1]

def dfs(now):
    # 현재 지나가는 곳은 다 1로 쳌
    visited[now] = 1

    for next in graph[now]:
        # 이미 지나갔던 곳으로 체크되어있으면 건너뛰고 계속
        if(visited[next] == 1):
            continue
        # 다음 노드 계속 탐색하기
        dfs(next)
# 1번 컴부터 탐색이니까
dfs(1)
print(sum(visited)-1)
