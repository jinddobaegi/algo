# 문제를 도저히 이해할 수가 없어서 이분 그래프 정의 찾아봄
# 이분 그래프(Bipartite Graph)란 인접한 정점끼리 서로
# 다른 색으로 칠해서 모든 정점을 두 가지 색으로만 칠할 수 있는 그래프

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

K = int(input())

def dfs(i):
    global bg

    # 연결된 노드 탐색
    for j in arr[i]:
        if visited[j] == 0:
            # 색을 1, 2로 칠하기
            # 인접한 노드는 현재 노드 색 반대로 칠하기
            if visited[i] == 1:
                visited[j] = 2
            elif visited[i] == 2:
                visited[j] = 1
            dfs(j)

        # 현재 노드와 인접한 노드 색이 같다면 이분 그래프 아님
        if visited[j] == visited[i]:
            bg = 1

for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    bg = 0

    for _ in range(E):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)

    for i in range(1, V+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)

            # 이분 그래프 아니면 바로 break
            if bg == 1:
                break

    if bg == 0:
        print('YES')
    else:
        print('NO')