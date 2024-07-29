# 순회공연

# n = int(input())
# cost = []
# max_cost = [0 for _ in range(n + 1)]
#
# for _ in range(n):
#     p, d = map(int, input().split())
#     cost.append((p, d))
#
# for p, d in cost:
#     if max_cost[d] < p:
#         max_cost[d] = p
#
# print(sum(max_cost))

from heapq import heappush, heappop

n = int(input())
cost = []
max_cost = []

for _ in range(n):
    p, d = map(int, input().split())
    cost.append((p, d))

cost.sort(key=lambda x: x[1])

for p, d in cost:
    heappush(max_cost, p)
    if (len(max_cost)) > d:
        heappop(max_cost)

print(sum(max_cost))