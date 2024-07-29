import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 순서대로 처리위해 마감일 기준으로 정렬
arr.sort(key=lambda x: x[1])
pq = []

# p 강연료 d 마감일
for p, d in arr:
    heapq.heappush(pq, p)
    if (len(pq) > d):  # pq 길이가 마감일보다 길어지면
        heapq.heappop(pq)  # 최소 강연료 제거

print(sum(pq))