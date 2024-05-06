from sys import stdin
from itertools import combinations

input = stdin.readline


def dfs():
    pass


N = int(input())  # 도시의 수
populations = list(map(int, input().split()))  # 1~N번 구역의 인구

adj_list = list(list() for _ in range(N+1))  # 1~N번 구역 인접 리스트
for _ in range(N):
    x, *adj_cities = map(int, input().split())
    adj_list.append(adj_cities)

# 도시를 두 부분으로 나눠서
# adj_list와 bfs/dfs를 통해 끊긴 부분이 있는지 check (visited가 다 찍히는지 보자)
# 끊긴 부분이 없다면, 두 부분의 인구 총합의 차를 구해서 최소가 되도록 한다

# 1) 두 부분집합으로 나누기
cities = list(x for x in range(1, N+1))
for i in range(1, N):
    A_list = list(combinations(cities, i))  # i개를 뽑은 부분집합의 모임, i: 1 ~ N-1
    for A in A_list:
        B = set(cities) - set(A)

        # 2) 각 부분집합 dfs 돌기
        visited = [0] * (N+1)
        # 2-1) A에 대해 dfs
        # 2-2) B에 대해 dfs

        # if visited 조건 안 맞으면:
            # continue

        # 3) 두 부분 인구 총합 구하기, 차 구해서 최솟값으로 갱신
        # 3-1) A, for문 돌면서 인구 총합
        # 3-2) B, for문 돌면서 인구 총합
