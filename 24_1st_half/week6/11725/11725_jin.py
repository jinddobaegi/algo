# 트리의 루트는 1
# 각 노드의 부모를 구하자
# N으로 노드 개수 주어짐
# 둘 째 줄부터 N-1개의 줄에 간선 정보 주어짐
# 결과적으로 2,3,4,5...값을 가진 노드들의 부모 노드 값을 출력!

from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())

adj_list = list(list() for _ in range(N+1))

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

parents = [0]*(N+1)
visited = [0]*(N+1)
q = deque()
q.append(1)
visited[1] = 1
tree = [0]*(N+1)


def bfs():
    while q:
        v = q.popleft()
        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
                tree[w] = v


bfs()
for i in range(2,N+1):
    print(tree[i])





# 반례 있음
# input으로 이전에 나온 적 없던 애들이 나오면 안됨
# parents = [0] * (N+1)  # 인덱스 -> 자식, 값은 부모
#
# visited = set()
# visited.add(1)
#
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#     if v1 in visited:
#         p = v1
#         c = v2
#     else:
#         p = v2
#         c = v1
#     visited.add(c)
#     parents[c] = p
#
#
# for i in range(2, N+1):
#     print(parents[i])


# Key Error
# my_dict = dict()  # 자식을 키로 하자
# visited = set()
# visited.add(1)
#
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#     if v1 in visited:
#         p = v1
#         c = v2
#     else:
#         p = v2
#         c = v1
#
#     visited.add(c)
#     my_dict[c] = p

# for i in range(2, N+1):
#     print(my_dict[i])


# 메모리 초과
# arr = list([0] * (N+1) for _ in range(N+1))
# 
# parents = [1]
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#     if v1 not in parents:
#         p = v2
#         c = v1
#         parents.append(v1)
#     else:
#         p = v1
#         c = v2
#         parents.append(v2)
# 
#     arr[p][c] = 1
# 
# for child in range(1, N+1):
#     for i in range(1, N+1):
#         if arr[i][child] == 1:
#             print(i)
#             break


# 시간 초과

# 2차원 배열
# 부모 -> 행 번호
# 자식 -> 그 행 배열의 원소로

# arr = list(list() for _ in range(N+1))
# parents = [1]  # 부모로 쓰인 적 있는지 체크
#
# for _ in range(N-1):
#     v1, v2 = map(int, input().split())
#
#     # 부모 자식 구분
#     if v1 not in parents:
#         p = v2
#         c = v1
#         parents.append(v1)
#     else:
#         p = v1
#         c = v2
#         parents.append(v2)
#
#     arr[p].append(c)
#
#
# for turn in range(2, N+1):
#     for i in range(1, N+1):
#         if turn in arr[i]:
#             print(i)
#             break
