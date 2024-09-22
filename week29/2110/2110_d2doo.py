# 공유기 설치
# 이진 탐색(한 공유기가 다른 집까지 수신 할 수 있는 최소 보장되는 거리가 최대한 넓어야함)

def binary_search(small, large):
    global dist
    while small <= large:
        mid = (small + large) // 2 # 최소 보장되는 거리
        house = houses[0]
        cnt = 1 # 공유기 개수

        for i in range(1, len(houses)):
            # 마지막으로 공유기를 설치한 집에서 다음 집까지 거리가 mid 이상이면 공유기 설치
            if houses[i] >= house + mid:
                cnt += 1
                house = houses[i] # 마지막으로 설치한 집 갱신

        if cnt >= C: # 공유기 설치 더 할 수 있는 경우
            small = mid + 1 # 이진 탐색이니까 small += 1을 하면 안됨 완전 탐색이 되어버림
            dist = mid
        else:
            large = mid - 1 # 공유기 설치 거리 좁혀야 하는 경우

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

small = 1 # 최소 거리
large = houses[-1] - houses[0] # 최대 거리
dist = 0

binary_search(small, large)

print(dist)