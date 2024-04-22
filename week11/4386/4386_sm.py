# 별자리 만들기
# 골드3

# 문제
# 도현이는 우주의 신
# 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것.
# 별자리의 조건
# 1. 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 3. 별들이 2차원 평면 위에 놓여 있다.
# 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.


# 전략
# 다익스트라
# 걍 갈 수 있는 모든 점 거리 계산하고 최소인 점으로 ㄱ
# 로 코드 짜려고 했는데 개가티 실패
# 유니온 파인드로 접근 슛
# 별자리 간 거리를 오름차순 정렬하고 연결 유무는 유니온 파인드로 확인


import sys
input = sys.stdin.readline

import math
# sys.setrecursionlimit(10 ** 6)

# 일단 유니온 파인드 함수 써
def find(x):
    if x == parent[x]:
        return x
    # 두개의 집합을 하나로 압축
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y



n = int(input())

# 별 좌표 담을 리스트
stars = []
lst = []
parents = [i for i in range(n+1)]
for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

# 두 별 간 거리 계산
for i in range(n-1):
    for j in range(i, n):
        # round(number, ndigits) : 이게 뭘까 싶어서 찾아봄
        # 소수점 반올림하는 함수
        # 루트(x2-x1) 제곱 + (y2-y1) 제곱
        distance = round(math.sqrt((stars[i][0] - stars[j][0]) **2 + (stars[i][1] - stars[j][1]) **2), 2)
        #자기자신으러 가는 건 계산 x 패스함
        if i == j:
            continue

        # 양방향 저장
        lst.append((distance, i, j))
        lst.append((distance, j, i))

# 거리 기준으로 정렬
lst.sort(key=lambda x: x[0])
# 부모 초기화
parent = list(range(n+1))


money = 0

for c, a, b in lst:
    if find(a) != find(b):
        union(a, b)
        money += c
print(money)

