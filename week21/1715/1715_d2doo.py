# 카드 정렬하기
# 가장 작은 묶음
import heapq

N = int(input())
card_lst = []
total = 0

for _ in range(N):
    heapq.heappush(card_lst, int(input()))

while len(card_lst) > 1:
    card1 = heapq.heappop(card_lst) # 작은거 하나 꺼내주고
    card2 = heapq.heappop(card_lst) # 그 다음으로 작은거 꺼내주고
    sum_card = card1 + card2

    total += sum_card
    heapq.heappush(card_lst, sum_card)

print(total)