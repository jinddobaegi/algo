# 문제
# 도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다. 하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다. 그런데 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다. (a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다. a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)

# 그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야 컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다. 이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 모든 컴퓨터를 연결할 수 없는 경우는 없다.

# 입력
# 첫째 줄에 컴퓨터의 수 N (1 ≤ N ≤ 1000)가 주어진다.

# 둘째 줄에는 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)가 주어진다.

# 셋째 줄부터 M+2번째 줄까지 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용이 주어진다. 이 비용의 정보는 세 개의 정수로 주어지는데, 만약에 a b c 가 주어져 있다고 하면 a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 든다는 것을 의미한다. a와 b는 같을 수도 있다.

# 출력
# 모든 컴퓨터를 연결하는데 필요한 최소비용을 첫째 줄에 출력한다.

# 예제 입력 1 
# 6
# 9
# 1 2 5
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8
# 예제 출력 1 
# 23

# 다익스트라로 실패
# import sys
# sys.stdin = open('week12/1922/1922.txt')
# input = sys.stdin.readline
# import heapq

# def dijkstra(start):
#     q = []
#     distance = [cost * 10000] * (computers+1)
#     distance[0] = 0
#     distance[start] = 0
#     heapq.heappush(q, (0, start))

#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue

#         for next, new_dist in graph[now]:
#             next_dist = dist + new_dist
#             if next_dist < distance[next]:
#                 distance[next] = next_dist
#                 heapq.heappush(q, (next_dist, next))

#     return sum(distance)
            


# computers = int(input())
# lines = int(input())
# graph = [[] for _ in range(computers+1)]

# for _ in range(lines):
#     start, end, cost = map(int, input().split())
#     graph[start].append((end, cost))
#     graph[end].append((start, cost))

# result = 9999999990000
# for i in range(1, computers+1):
#     go = dijkstra(i)
#     result = min(result, go)

# print(result)

import sys
sys.stdin = open('week12/1922/1922.txt')
input = sys.stdin.readline

def find_parent(parent, x): 
    if parent[x] != x: # 루트 노드가 아니라면
        parent[x] = find_parent(parent, parent[x]) # 루트 노드를 찾을 때까지 재귀적으로 호출
    return parent[x] # 루트 노드 반환

def union_parent(parent, rank, a, b):
    a = find_parent(parent, a) # a의 루트 노드를 찾는다
    b = find_parent(parent, b) # b의 루트 노드를 찾는다

    if rank[a] < rank[b]: # a 랭크가 작다면
        parent[a] = b # a의 부모를 b로 설정
    else: # a 랭크가 크다면
        parent[b] = a # b의 부모를 a로 설정
        if rank[a] == rank[b]: # 랭크가 같다면
            rank[a] += 1 # 랭크를 1 증가시킨다 

# 크루스칼 알고리즘을 위한 유니온-파인드 구현
computers = int(input())
lines = int(input())
graph = []

for _ in range(lines):
    a, b, c = map(int, input().split())
    graph.append((c, a-1, b-1))

graph.sort() # 비용 순으로 정렬 -> 왜냐하면 비용이 작은 순으로 연결해야 최소 비용이 나온다
parent = list(range(computers)) # [0, 1, 2, 3, 4, 5]  # 부모 테이블 초기화
rank = [0] * computers # [0, 0, 0, 0, 0, 0]  # 랭크는 0으로 초기화 -> 트리의 높이

result = 0
for cost, a, b in graph: # 비용 순으로 정렬된 그래프를 순회하면서 
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는다면 
        union_parent(parent, rank, a, b) # 두 노드를 연결하고
        # print("여기구나",parent,rank, a, b)
        result += cost # 비용을 더한다

print(result)








