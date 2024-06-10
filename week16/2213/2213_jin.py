N = int(input())  # 1~N: 트리의 정점
w_list = [0] + list(map(int, input().split()))  # 1~N까지 정점의 가중치
adj_list = list([] for _ in range(N+1))
visited = [0] * (N+1)
dp = list([0, 0] for _ in range(N+1))  # 포함/미포함 최댓값
selected = list([[], []] for _ in range(N+1))  # 포함/미포함 선택 노드

'''
dp[i][0]에는 i번 노드를 포함했을 때의 최대 크기를 지정
그럼 i의 자식이 n이랑 m이라고 가정하면
dp[i][0]에는 dp[m][1]과 dp[n][1]이 들어갈 것임
2번째 차원의 값 -> 0: 포함, 1: 미포함
따라서 임의로 루트노드 하나 잡고 (1이라고 하자)
dfs로 재귀적으로 가장 깊은 곳으로 가서 걔부터 dp를 채워나가는 식으로 갱신
그렇게 해서 최종적으로 빠져나올 때는 dp[1][0]과 dp[1][1]이 정해지면
그 중 큰 값이 답이 된다!
'''

for _ in range(N-1):
    v, w = map(int, input().split())
    adj_list[v].append(w)
    adj_list[w].append(v)


def dfs(p):
    visited[p] = 1
    dp[p][0] = w_list[p]
    selected[p][0].append(p)

    for c in adj_list[p]:
        if not visited[c]:
            dfs(c)
            # 1) 부모 선택하는 경우
            dp[p][0] += dp[c][1]  # 부모 선택했으니 자식은 선택 x
            selected[p][0].extend(selected[c][1])  # 자식의 경로 extend

            # 2) 부모 선택 안하는 경우
            # -> 특정 자식을 선택 / 미선택 중 큰 거 -> 부모의 dp에 저장
            # 즉 dp[p][1]에다가 큰 거!
            if dp[c][0] > dp[c][1]:
                dp[p][1] += dp[c][0]
                selected[p][1].extend(selected[c][0])
            else:
                dp[p][1] += dp[c][1]
                selected[p][1].extend(selected[c][1])


dfs(1)
num = 0 if dp[1][0] > dp[1][1] else 1
print(dp[1][num])
res = selected[1][num]
res.sort()
print(*res)


'''
시간초과 코드

from itertools import combinations

N = int(input())  # 1~N: 트리의 정점
w_list = [0] + list(map(int, input().split()))  # 1~N까지 정점의 가중치
adj_list = list([] for _ in range(N+1))

for _ in range(N-1):
    v, w = map(int, input().split())
    adj_list[v].append(w)
    adj_list[w].append(v)

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
            for other in adj_list[c]:
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
'''