import sys
sys.stdin = open('input.txt')
import heapq

n = int(input())
info = []
for _ in range(n):
    m, t = map(int, input().split())
    info.append([m, t])
new_info = sorted(info, key=lambda x: x[1])
# print(new_info)

pq = [] # 내가 갈 강연정보를 담음

for pay, limit in new_info:
    heapq.heappush(pq, pay)
    if len(pq) > limit: # len(pq)는 며칠 지났는지
        heapq.heappop(pq) # heapq가 오름차순정렬은 아닌데 가장첫번째가 가장 작은 값
# 일반 list는 pop하면 가장 오른쪽 값을 빼는데 heapq는 첫번째가 최소값확정이라 그거 뺌

print(sum(pq))

