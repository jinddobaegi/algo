# 실버1
# RGB 거리

# 문제
'''
집 n개
- 집은 r, g, b, 중 하나로 칠해야돼
규칙
1번 집 색 != 2번 집 색
N번 집 색 != N-1번 집 색
i번 집 색 != i-1, i+1
'''

# 로직
#dp
# 모든 집 칠하는 최소비용을 뽑아야함


import sys
sys.stdin = open("1149.txt")
input = sys.stdin.readline

n = int(input())
houses = []
for _ in range(n):
    r,g,b = map(int, input().split())
    houses.append([r,g,b])   # [[30, 19, 5], [64, 77, 64], [15, 19, 97], [4, 71, 57], [90, 86, 84], [93, 32, 91]]


for i in range(1, n):
    # 1번 집부터 동적 탐색하자
    # i번쨰 집 기준으로 전부다 탐색해서 최솟값을 찾는거야
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])  # i가 r
    houses[i][1] += min(houses[i-1][2], houses[i-1][0])  # i가 g
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])  # i가 b

# 그 중에 젤 적은 비용 뽑아
cost = min(houses[n-1])
print(cost)