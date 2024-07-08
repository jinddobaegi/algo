# 별자리 만들기
# 누가 냈냐 이거
# 다익스트라? 유니온 파인드?
# 크루스칼...
# 거리 계산 (x1-x2)^2 + (y1- y2)^2
import math # 제곱근 계산하기위해

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
arr = []
position = [] # (노드1, 노드2, 가중치)
parent = [i for i in range(n+1)]

for _ in range(n):
    x, y = map(float, input().split())
    arr.append((x, y))

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        position.append((i, j, math.sqrt((x1 - x2)**2 + (y1 - y2)**2))) # 거리 계산

position.sort(key=lambda x: x[2]) # 빼먹지 말기 흑흑

ans = 0
for a, b, c in position:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += c

print(round(ans, 2)) # 소수점 자리에 맞춰 반올림