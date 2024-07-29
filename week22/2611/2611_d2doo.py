# 자동차경주
# 위상정렬 설명해주실 분 구합니다
# 방향이 있어야하고 사이클이 있어야함..?

N = int(input()) # 지점의 개수 N
M = int(input()) # 도로의 개수 M
road = []

for _ in range(M):
    p, q, r = map(int, input().split())
    road.append((p, q, r)) # p -> q 도로가 존재하고 cost는 r

