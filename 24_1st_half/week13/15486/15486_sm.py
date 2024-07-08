# 퇴사 슛
# 문제가 너무 길어서... 안 썼어유..

from sys import stdin

# 일.
N = int(input())

# 최대 수익 리스트 초기화
profit = [0] * (N + 1)

for i in range(1, N + 1):
    # 수익. 시간
    t, p = map(int, input().split())

    # 최대수익 업뎃
    profit[i] = max(profit[i - 1], profit[i])

    # 현재 날짜에 작업 시작 - 종료 가능한지부터 체크
    if i + t <= N + 1:
        # 작업 시작하여 종료하는 것이 수익 더 많으면 업뎃
        profit[i + t - 1] = max(profit[i - 1] + p, profit[i + t - 1])

print(profit[-1])
