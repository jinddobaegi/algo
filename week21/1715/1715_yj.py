import heapq

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

# 계속해서 작은 묶음 찾아서 더해주기
ans = 0
while len(arr) != 1:
    c1 = heapq.heappop(arr)
    c2 = heapq.heappop(arr)
    sum_c = c1 + c2
    ans += sum_c
    heapq.heappush(arr, sum_c)

print(ans)