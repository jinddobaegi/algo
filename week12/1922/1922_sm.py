# 네트워크 연결
# 골드 4
# 문제
# 도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다.
# 하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다.
# 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다.
# (a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다.
# a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)
# 그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야
# 컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다.
# 이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라.
# 모든 컴퓨터를 연결할 수 없는 경우는 없다.

# 유니온 파인드 슛

import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 컴퓨터
N = int(input())
# 연결 선 수
M = int(input())

parent = [i for i in range(N+1)]

lst = []
for _ in range(M):
    a, b, c = map(int, input().split())
    lst.append((c, a, b))

lst.sort()
ans =  0 # 출력할 최소비용


for l in lst:
    c, a, b = l
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += c


print(ans)