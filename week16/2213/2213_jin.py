from itertools import combinations

N = int(input())  # 1~N: 트리의 정점
w_list = [0] + list(map(int, input().split()))  # 1~N까지 정점의 가중치
edge = list([] for _ in range(N+1))

for _ in range(N-1):
    v, w = map(int, input().split())
    edge[v].append(w)
    edge[w].append(v)

# 독립집합: 집합에 속한 정점이 모두 인접하지 않는 집합
# 최대독립집합: 가중치가 다르다면 가중치의 합이 가장 큰 경우, 동일하다면 정점의 개수가 가장 많은 경우

# 조합 나누고
# 인접해있는지 판단하면 되지 않나?
max_v = 0
res = tuple()
for r in range(1, N+1):
    node_combies = combinations(range(1, N+1), r)
    for combi in node_combies:
        # combi 하나에 원소들이 들어있음
        is_possible = True
        tmp = 0
        for c in combi:
            if not is_possible:
                break
            tmp += w_list[c]
            for other in edge[c]:
                if other in combi:
                    is_possible = False
                    tmp = 0
                    break

        if is_possible:
            if max_v < tmp:
                max_v = tmp
                res = combi

print(max_v)
print(*res)