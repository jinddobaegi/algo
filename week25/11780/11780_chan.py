import sys
sys.stdin = open("week25/11780/11780.txt")
input = sys.stdin.readline

N = int(input())
M = int(input())

city_map = [[float("inf")] * N for _ in range(N)]

for i in range(N):
    city_map[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1

    if city_map[a][b] > c:
        city_map[a][b] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            if city_map[i][j] > city_map[i][k] + city_map[k][j]:
                city_map[i][j] = city_map[i][k] + city_map[k][j]

for i in range(N):
    for j in range(N):
        if city_map[i][j] == float("inf"):
            print(0, end=" ")
        else:
            print(city_map[i][j], end=" ")
    print()