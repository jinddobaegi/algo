import sys
sys.stdin = open('input.txt')
import heapq

n = int(input())
cards = []
for _ in range(n):
    a = int(input())
    heapq.heappush(cards, a)
# print(cards)
ans = 0
while len(cards) > 1: # 두개씩 꺼내서 확인하니까 1보다 커야함
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    card = x + y
    ans += card
    heapq.heappush(cards, card)
    # heapq가 가중치낮은거 순서대로 정렬해주니까 내가 위에서 꺼내는 x, y는
    # cards에서 가장 작은 2개의 수가 됨

    # print(cards)
print(ans)



