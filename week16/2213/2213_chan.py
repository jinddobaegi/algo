import sys
sys.stdin = open("week16/2213/2213.txt")
input = sys.stdin.read
from collections import defaultdict
sys.setrecursionlimit(100000)

def dfs(u):
    # 12. 현재 정점 u에서 독립 집합의 최대 크기를 계산.
    dp[u][0] = 0
    dp[u][1] = weights[u]
    
    for v in tree[u]:
        if v != parent[u]:  # 13. 부모 노드를 제외하고 자식 노드를 탐색
            parent[v] = u  # 14. 부모 노드를 설정
            dfs(v)  # 15. 자식 노드로 DFS를 수행
            dp[u][0] += max(dp[v][0], dp[v][1])  # 16. 정점 u가 독립 집합에 포함되지 않을 때 최대값 갱신
            dp[u][1] += dp[v][0]  # 17. 정점 u가 독립 집합에 포함될 때 최대값 갱신

def trace(u, include): #최대 독립 집합을 추적하는 함수
    if include:
        result.append(u)  # 18. 정점 u를 결과에 추가합니다.
        for v in tree[u]:
            if v != parent[u]:
                trace(v, False)  # 19. 자식 노드를 독립 집합에 포함시키지 않고 탐색합니다.
    else:
        for v in tree[u]:
            if v != parent[u]:
                if dp[v][0] >= dp[v][1]:
                    trace(v, False)  # 20. 자식 노드가 독립 집합에 포함되지 않을 때 탐색.
                else:
                    trace(v, True)  # 21. 자식 노드가 독립 집합에 포함될 때 탐색.

data = input().split()  # 2. 입력 데이터를 읽어옵니다.
n = int(data[0])  # 3. 트리의 정점 수를 가져옵니다.
weights = [0] + list(map(int, data[1:n+1]))  # 4. 각 정점의 가중치를 가져옵니다.

tree = defaultdict(list)  # 5. 트리를 표현할 defaultdict를 생성합니다.
index = n + 1
for _ in range(n - 1):
    u, v = int(data[index]), int(data[index + 1])  # 6. 간선 정보를 가져옵니다.
    tree[u].append(v)  # 7. 트리의 간선을 추가합니다.
    tree[v].append(u)  # 8. 트리의 간선을 추가합니다.
    index += 2  # 9. 다음 간선으로 인덱스를 이동합니다.
print(tree)

dp = [[0, 0] for _ in range(n + 1)]  # 10. DP 테이블을 초기화합니다.
# dp[u][0]: 정점 u가 독립 집합에 포함되지 않을 때 최대값
# dp[u][1]: 정점 u가 독립 집합에 포함될 때 최대값
parent = [-1] * (n + 1)  # 11. 부모 노드를 저장할 배열을 초기화.

dfs(1)  # 22. 루트 정점 1에서 DFS를 시작합니다.

result = []
if dp[1][0] >= dp[1][1]:  # 23. 루트 정점에서의 최대 독립 집합의 크기를 비교합니다.
    trace(1, False)  # 24. 루트 정점이 포함되지 않은 경우의 독립 집합을 추적합니다.
else:
    trace(1, True)  # 25. 루트 정점이 포함된 경우의 독립 집합을 추적합니다.

result.sort()  # 26. 결과 정점을 오름차순으로 정렬합니다.

print(max(dp[1][0], dp[1][1]))  # 27. 최대 독립 집합의 크기를 출력합니다.
print(" ".join(map(str, result)))  # 28. 최대 독립 집합에 속한 정점을 출력합니다.