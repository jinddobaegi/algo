from sys import stdin
from heapq import heappush, heappop

input = stdin.readline

N = int(input())  # 대학의 수
lectures = list(tuple(map(int, input().split())) for _ in range(N))  # p, d 순
lectures.sort(key=lambda x: x[1])  # 마감기한 짧은 순 정렬

# d가 겹치는 강연들은
# 그 기한 안에 몇 개를 할 수 있는지가 관건

# 로직 3
# j일째에는 최대 j개의 강의 선택 가능
# + 찾아보니 힙큐를 이용하더라
# 강의를 하나씩 보자

pq = []
for p, d in lectures:
    heappush(pq, p)
    # pq의 길이, 즉 선택한 강의 개수와
    # 현재 강의의 기한을 비교
    # 만약 강의 기한이 선택한 강의보다 크거나 같아야 함
    if d < len(pq):
        heappop(pq)

print(sum(pq))

'''
이게 안되네
3
10 1
20 2
30 2

정답 50
'''

# 로직 2 -> 실패, 뭔가 이상함
# 냅색처럼 풀어보자
# i번째 강의에 대해
# n일차에 최대로 얻을 수 있는 돈 계산

# dp = [[0]*(N+1) for _ in range(N+1)]  # 행: 강의, 열: 날짜
#
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         p, d = heappop(pq)
#         p = -p
#         # j일째에는 최대 j개의 강의 선택 가능함
#         # 내가 j일째에 i번째 강의를 선택할 수 있는가?
#         # 1) 선택 불가능
#         if j < d:
#             dp[i][j] = dp[i-1][j]
#         # 2) 선택 가능
#         else:


# 로직 1 -> 실패
# 마지막 날짜를 갱신하는 주기를 언제로 해줘야 할까?
# 강연 기한 확인
# -> 마지막 강연 날짜보다 작거나 같으면 못함(어차피 금액순으로 정렬돼있어서 날짜가 같으면 앞에꺼가 큰 거임)
# 마지막 강연 날짜보다 크면 마지막 강연날짜+1 후 강연 함

# total = 0
# last_d = 0
# for d, p in lectures:
#     p = -p
#     if d > last_d:
#         total += p
#         last_d += 1
#
# print(total)