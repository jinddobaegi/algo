import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
inf = float('inf')
distance = [[inf] * (n+1) for _ in range(n+1)]
route = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    distance[s][e] = min(distance[s][e], c)

for i in range(1, n+1):
    distance[i][i] = 0
# for m in distance:
#     print(m)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
            if distance[a][k] + distance[k][b] < distance[a][b]:
                distance[a][b] = distance[a][k] + distance[k][b]
                route[a][b] = k # route[a][b]의 값은 경유지

# 위 3중 for문에서 최소값들을 다 갱신하는데
# 입력값중에 어느 방법으로든 갈 수 없는 도시가 있을 수도 있음 => inf로 남아있으면 0으로 바꿔주기
for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == inf:
            distance[i][j] = 0

# for x in route:
#     print(x)
# routes[s][e] 값이 0이면 s에서 e로 갈 때 다른 도시를 경유하지 않고 바로가는게 베스트

def find_path(s, e):
    if route[s][e] == 0: #
        return []
    k = route[s][e] # 저장해놓은 경유지를 꺼내와서
    return find_path(s, k) + [k] + find_path(k, e)

# 정답출력

for i in range(1, n+1):
    ans = distance[i][1:]
    print(*ans)

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == 0:
            print(0)
            continue
        path = [i] + find_path(i, j) + [j]
        print(len(path), end=" ")
        print(*path)

# # 출력값이
# 2 1 2 면
# 2개, 1 - 2 경로
# 2 1 3 이면
# 2개 1 - 3 경로라는 뜻
