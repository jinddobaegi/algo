import sys
sys.stdin = open('input.txt')

n, d = map(int, input().split())

shortcut_info = []
for _ in range(n):
    s, e, dist = map(int, input().split())
    shortcut_info.append([s, e, dist])
# print(shortcut_info)

distance = [0]*(d+1)
distance[0] = 0
# 일단 지름길 없이 각 지점별 길이 다 입력
for i in range(1, d+1):
    distance[i] = distance[i-1] + 1
# print(distance)
for i in range(1, d + 1):
    # 지름길이 없다면
    # 예를들어 100까지의 거리는 99에서 +1 한거
    distance[i] = distance[i-1] + 1

    # 지름길이 있다면
    for s, e, dist in shortcut_info:
        if e == i:
            distance[i] = min(distance[i], distance[s] + dist)

print(distance[d])