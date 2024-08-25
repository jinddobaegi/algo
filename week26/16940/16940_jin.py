from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
adj_list = list(set() for _ in range(N+1))
adj_list[0].add(1)
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_list[a].add(b)
    adj_list[b].add(a)

route = tuple(map(int, input().split()))

# 어차피 bfs는
# 같은 깊이에 있는 것들을 다 돌고 난 뒤
# 그 다음 깊이의 노드를 돌 수 있다

def bfs():
    q = deque()
    q.append(0)
    front = 0  # 디큐 느낌으로 쓰는 것
    for w in route:  # 주어진 노드 순서대로 확인해볼 것임
        # 프론트 노드의 자식 중 w를 찾을 때까지 돎
        while w not in adj_list[q[front]]:
            front += 1  # 프론트 노드 자식 중에 w 없으면 디큐
            if front == len(q):  # 큐가 빈 상태
                return 0
        q.append(w)  # 프론트의 자식 중 w가 있어서 while문 빠져나오고 인큐
        
    return 1  # for 문을 다 돌았다? == 마지막 경로까지 append 됐다


print(bfs())

# 첫 노드(시작점)를 하나 뽑음
# 거기서 갈 수 있는 곳 묶어서 enqueue, 방문표시
# 다음 목적지는 그 묶음 안에 있어야 함
# 그 노드를 찾았다? 그럼 그 묶음 안에서 해당 노드만 제거하고
# 해당 노드에서 이동 가능한 노드들 묶어서 enqueue
# 반복

# 시간 초과
# q = list(set() for _ in range(N+1))  # 단계 별로 저장할 것임
# visited = [0] * (N+1)
# q[1].add(1)
# visited[1] = 1
# depth = 1
# idx = 0
# while depth != N:
#     if not q[depth]:
#         depth += 1
#         continue
#     x = route[idx]
#     v = 0
#     if x in q[depth]:
#         v = x
#         q[depth].remove(v)
#         idx += 1
#         for w in adj_list[v]:
#             if not visited[w]:
#                 q[depth + 1].add(w)
#                 visited[w] = 1
#     else:
#         break
#
# print(int(idx == N))