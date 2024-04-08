# 문제
# 트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
# 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
# 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.



# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.

# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.



# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

# 입력
# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다.
# 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다.
# 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 
# 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.


import sys
sys.stdin = open("1967.txt")
input = sys.stdin.readline

def bfs(start):
    visited = [-1] * (totalnode + 1)
    visited[start] = 0
    stack = [start]
    while stack:
        node = stack.pop()
        for next_node, weight in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + weight
                stack.append(next_node)
    print(visited)
    return visited

totalnode = int(input())
graph = [[] for _ in range(totalnode+1)]
for _ in range(totalnode - 1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# 1에서 가중치가 가장 큰 인덱스를 찾고 그인덱스에서 가장 가중치가 큰 노드를 찾는다.
start = 1 #항상 1이라고 가정
result = bfs(start) #1에서 가장 먼 노드 찾기
start = result.index(max(result)) 
result = bfs(start)
print(max(result))













