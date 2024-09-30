import sys
sys.stdin = open('input.txt')
from collections import deque

n = int(input())
works = []
for _ in range(n):
    w = list(map(int, input().split()))
    works.append(w)

# for m in works:
#     print(m)

# 1. 선행작업 개수 표시
pre = [0] * (n+1)
dp = [0] * (n+1) # dp[i]는 i번 작업이 완료된 시간
graph = [[] for _ in range(n+1)] # 각 작업의 선행작업

for i in range(n):
    pre[i+1] = works[i][1]
    if pre[i+1] > 0:
        for j in works[i][2:]:
            graph[j].append(i+1)

# for m in graph:
#     print(m)

def sol():
    q = deque()

    for i in range(1, n+1): # 1번작업만 선행없다는 가정x
        if pre[i] == 0:
            q.append(i)
            dp[i] = works[i-1][0]

    # print(dp)
    while q:
        cur = q.popleft()

        for nw in graph[cur]:
            pre[nw] -= 1
            dp[nw] = max(dp[nw], dp[cur] + works[nw-1][0])
            # print(dp)
            if pre[nw] == 0:
                q.append(nw)

sol()
print(max(dp))
# print(pre)

# import sys
# sys.stdin = open('input.txt')
# from collections import deque
#
# n = int(input())
# works = []
# for _ in range(n):
#     w = list(map(int, input().split()))
#     works.append(w)
#
# # for m in works:
# #     print(m)
#
# # 1. 선행작업 개수 표시
# pre = [0] * (n+1)
#
# for i in range(n):
#     pre[i+1] = works[i][1]
#
# # print(pre)
#
# def sol():
#     q = deque()
#     ans = 0
#     res = []
#
#     for i in range(1, n+1):
#         if pre[i] == 0:
#             q.append(i)
#
#     while q:
#         cur = q.popleft() # 현재 진행할 작업번호
#         res.append(works[cur - 1][0])
#         visited[cur] = True # 작업 처리 표시
#
#         print(f"처리한 작업:{cur}, 누적시간:{res}")
#         # 여기서 1, 2, 4 작업을 처리하면 res가 12가 아니고 11이 나와야함
#         # print(cur)
#         # print(q)
#         # 전체 작업들을 확인하면서 1번 작업이 선행조건이면 pre에서 한개 없애줌
#         for i in range(2, n+1):
#             if not visited[i]:
#                 # print(f"현재 {i}번 노드검사중, 선행노드들은 {works[i-1][2:]}, cur는 {cur}")
#                 if cur in works[i-1][2:]:
#                     pre[i] -= 1
#                     if pre[i] == 0:
#                         q.append(i)
#
#         print(res)
#                         # 위에까지 선행작업 개수 줄여주기를 하고 더이상 선행작업이 없으면
#                         # q에 넣어서 진행할 작업으로 옮겨주기
#         # 동시수행 처리를 어떻게 함?
#         # q에 담기는 애들은 당장 시작 가능한 애들 => 동시처리 가능
#         # q에 2개 이상 들어있으면 전부다 동시에 작업을 처리해서
#         # 값이 가장 큰 애만 res에 더해줘야함
#
#
#     return res
# visited = [False] * (n+1)
# print(sol())

