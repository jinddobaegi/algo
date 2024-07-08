from sys import stdin
from pprint import pprint

input = stdin.readline

# 1) 출발 도시 정하기 -> 어디든 상관 없음, 따라서 0번으로 가정
# 2) 방문여부 -> 비트마스킹
# 3) dp[i][route]
#    현재위치 i에서 route(거쳐온 도시들)를 지나왔을 때 드는 최소 비용
#    그럼 dp의 행은 N개, 열은 2^N개

# https://hongcoding.tistory.com/83
# https://simsim231.tistory.com/199


def tsp(now, route):
    if route == (1 << N) - 1:  # (2^N) -1: 모든 경로를 돌았나?
        if arr[now][0]:  # 거기서 0으로 가는 길이 있을 때
            return arr[now][0]  # 그거 반환
        else:  # 현재 위치에서 0으로 가는 길이 없을 때
            return INF

    if dp[now][route] != 0:  # 이미 와본 적 있을 경우
        return dp[now][route]  # 저장된 메모이제이션 값 활용

    min_v = INF
    for i in range(1, N):  # 출발 도시 제외하고
        if not arr[now][i]:  # 현재 도시에서 i 도시로 가는 경로 없는 경우
            continue

        if route & (1 << i):  # i 도시가 이미 방문한 도시인 경우
            continue

        # 현재 도시에서 i 도시로 가는 경로가 있고
        # 방문하지 않은 경우
        # 현재 도시까지 오는 값을 갱신해줄 것임

        dist = arr[now][i] + tsp(i, route | (1 << i))
        min_v = min(min_v, dist)

    dp[now][route] = min_v

    return min_v


N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
INF = int(1e8)
dp = list([0] * (1 << N) for _ in range(N))  # 열 개수가 0 ~ (2^N)-1까지 2^N개임 -> 출발 도시 포함!

print(tsp(0, 1 << 0))

# 참고로 "|(or)" 연산자는 비트를 추가하는 효과가 있다!
# route: 1001, i가 2 즉 0100이라면
# route | (1<<2) == "1001 | 0100"
# 결과는 1101이 된다

# 그와 비슷하게 비트를 끌 때는 and와 not을 섞어서
# route & ~(1<<i) 이런 식으로 하면 된다