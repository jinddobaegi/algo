# 조합으로 선거구 나누기
# 조합별로 dfs 탐색해서 인접한지 아닌지 판단
# 다 인접하면 인구 차이 구하기

from itertools import combinations

N = int(input())  # 구역의 개수
p = [0] + list(map(int, input().split()))  # 인구 수
arr = [[] for _ in range(N+1)]  # 인접 구역 정보
temp = [i for i in range(1, N+1)]
min_diff = float('inf')

def dfs(lst, start, visited):
    p_sum = p[start]
    visited.append(start)

    for e in arr[start]:   # 인접한 구역 탐색
        if e in lst and e not in visited:  # lst에 있고 방문한 적 없으면
            p_sum += dfs(lst, e, visited)

    return p_sum

for i in range(1, N+1):
    nodes = list(map(int, input().split()))
    arr[i] = nodes[1:]

for i in range(1, N//2 + 1):  # 인구 차이 최소화하기 위해 절반 이하 크기의 조합 구하기
    for value in combinations(temp, i):
        temp1 = []  # combinations로 나온 조합
        temp2 = [i for i in range(1, N + 1)]  # 나머지 조합

        for j in value:
            temp1.append(j)
            temp2.remove(j)

        visited1 = []
        visited2 = []

        arr1 = dfs(temp1, temp1[0], visited1)
        arr2 = dfs(temp2, temp2[0], visited2)

        # 길이가 같다면 구역을 다 방문한 것
        if len(visited1) == len(temp1) and len(visited2) == len(temp2):
            if abs(arr1 - arr2) < min_diff:
                min_diff = abs(arr1 - arr2)

ans = min_diff
if ans == float('inf'):
    ans = -1

print(ans)