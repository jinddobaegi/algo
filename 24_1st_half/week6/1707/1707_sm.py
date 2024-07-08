# 이분 그래프
# 골드 4

# 일단 문제

# 그래프 정점의 집합을 둘로 분할
# 각 집합에 있는 정점끼리는 서로 인접 안하게 분할 -> 이거시 이분 그래프

# 조건별로 출력할 거임
# - 정점끼리 인접 안 하면 YES
# - 인접하면 NO

import sys


# 로직이 성립이 안 된다 갈아엎자
# def dfs(start, nextto, visited, set_lst):
#     visited[start] = True  # 방문하는 곳 쳌
# 
#     for i in nextto[start]:
#         # 정점이 방문하지 않았으면
#         if not visited[i]:
#             # 현재 정점 start 와 인접한 정점 i 를 서로 다른 그룹에 속하게 설정
#             set_lst[i] = (set_lst[start]+1) % 2
#             # 그러고 탐색 ㄱ
#             dfs(i, nextto, visited, set_lst)
#         elif set_lst[start] == set_lst[i]:  # 현재 정점이 인접 정점이랑 같으면
#             
# 
# 
# # tc 개수
# K = int(input())
# for _ in range(K):
#     # 정점, 간선
#     V, E = map(int, input().split())
# 
#     # 인접 리스트 담을 빈 그래프
#     nextto = [[] for _ in range(V+1)]
#     # 방문 체크할 리스트
#     visited = [False] * (V+1)
# 
#     # 집합을 둘로 분할할 리스트도 있어야 할 듯...?
#     set_lst = [0] * (V+1)
#     
#     # 판별하는 변수
#     check = True
#     
#     # 간선 정보
#     for _ in range(E):
#         u, v = map(int, input().split())
#         # 그래프에 샥샥 담아 (연결된 노드끼리)
#         nextto[u].append(v)
#         nextto[v].append(u)
#         # [[], [3], [3], [1, 2]] -> 이런 식으로 담기게 됨
#         # [[], [2], [1, 3, 4], [2, 4], [3, 2]]
# 
#     for i in range(1, V+1):
#         if check:
#             dfs(i, nextto, visited, set_lst)
#         else:
#             break
#     if True:
#         print("YES")
#     else:
#         print("NO")


# 아  안 풀리는 군

# 그러면 지나간 자리의 값들을 1, -1로 다르게 표시해서 인접한 자리의 수가 같은 수면 no
# 저 로직 쓰고 싶은데 코드를 못 짜겠어서 포기..
K = int(input())
for _ in range(K):
    # 정점, 간선
    V, E = map(int, input().split())

    # 인접 리스트 담을 빈 그래프
    nextto = [[] for _ in range(V+1)]
    # 방문 체크할 리스트
    visited = [False] * (V+1)

    