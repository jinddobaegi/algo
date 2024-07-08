# 게으른 백곰
# 실버3

import sys

# 문제
# 적은 거리만 움직이고 많은 얼음 먹을 것
# 우리 = 1차원 배열임 리스트임
# 자리 잡으면 그로부터 좌우로 K만큼 떨어진 곳까지 닿기 쌉가능

# 로직
# 좌표 값 중 가장 큰 값을 기준으로 하나하나 탐색하긔
# 좌우 K만틈 탐색하며 값 더해서 비교해보기

if __name__ == '__main__':
    N, K = map(int, input().split())
    # 비교하면서 갱신할 최댓값 최솟값
    max_v, min_v = 0, 100000
    graph = [0] * 1000001
    for _ in range(N):
        g, x = map(int, input().split())  # g: 얼음양 x: 양동이 좌표
        # 최댓값보다 크면 갱신
        if x > max_v:
            max_v = x
        # 최솟값보다 작으면 갱신
        if x < min_v:
            min_v = x
        # 해당 좌표에 있는 얼음
        graph[x] = g

    # k 이동벙위가 인덱스 범위 내에 없으면
    if min_v - K < 0:
        start = 0
    else:  # 범위 내에 있으면 start값을 그거로 변경해주기
        start = min_v - K

    end = start

    # 최종출력값
    sum_v, ans = 0, 0
    # 처음부터 max_v 까지 탐색하면서
    for i in range(start, max_v+1):
        while end <= 1000000 and end-i <= 2*K: # 크기는 최대 2* K로 제한할 것
            sum_v += graph[end]
            end += 1
        ans = max(ans, sum_v)
        sum_v -= graph[i]
    print(ans)
