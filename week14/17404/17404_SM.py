# RGB거리2
# 골드4

# 문제
'''
아까 풀었던 RGB거리 문제랑 다른 점
: 1번 집이 N번 집 색이 달라야돼
'''

#로직
# - 기본 로직은 비슷하게 가고 조건적으로 저 추가된 사항에 대한 판별하는게 들어가야할듯?


import sys
input = sys.stdin.readline

n = int(input())
houses = []
for _ in range(n):
    r,g,b = map(int, input().split())
    houses.append([r,g,b])

# 일단 초기값 세팅을 겁나 큰 걸로 해
# 그래야 갱신하지...
min_v = 1e9

# 색깔 3개
for i in range(3):
    dp = [[min_v, min_v, min_v] for _ in range(n)]
    # 1번째 집 각각 r,g,b로 칠하는 경우를 따로 계산해주고
    # 그러면 총 3가지 경우가 생기겠지..(까먹지 말고 마지막에 이거 갖다 써야돼)
    dp[0][i] = houses[0][i]

    # 2번째 집부터 끝까지는 체크하면서 최소비용 갱신해 (이 로직은 앞에1이랑 똑같이)
    for j in range(1, n):
        dp[j][0] = houses[j][0] + min(dp[j-1][1], dp[j-1][2]) # j번째 r
        dp[j][1] = houses[j][1] + min(dp[j-1][0], dp[j-1][2]) # j번쨰 g
        dp[j][2] = houses[j][2] + min(dp[j-1][0], dp[j-1][1]) # j번째 b

    # 다 돌고서 첫집이랑 마지막집 색이 같지 않은 경우만 비용 계산해
    for k in range(3):
        # 첫집을 i번쨰 칠한 색이랑 다른 경우만
        if i != k:
            # 최소비용 갱신
            min_v = min(min_v, dp[-1][k])

print(min_v)