import sys
sys.stdin = open("week22/2611/2611.txt")
input = sys.stdin.readline
import heapq

#입력
#첫째 줄에는 지점의 개수 N이 주어진다. 
#각 지점에는 1부터 N까지의 서로 다른 번호가 부여된다. 

#둘째 줄에는 도로의 개수 M이 주어진다. 
#이어 M개의 줄에는 p ,q ,r의 형식으로 도로의 정보가 주어지는데 이는 p번 지점부터 q번 지점으로 갈 수 있는 도로가 있고 그 도로에 부여된 점수가 r이라는 뜻이다.

#N은 1000이하의 자연수이고, p와 q는 1이상의 N이하의 자연수이며 r은 100이하의 자연수 이다. p와 q는 같지 않다.

#출력
#가장 많은 점수를 얻은 경로를 찾아, 첫째 줄에는 그 얻는 점수를 출력하고 둘째 줄에는 그 경로를 출력한다.
#경로를 출력할 때는 지나는 지점들의 번호를 사이에 한 칸의 공백을 두어 출력한다. 
#출력하는 경로는 반드시 1번 지점에서 시작하여 1번 지점으로 끝나야 한다. 
#만약 같은 점수를 얻는 경로가 둘 이상일 경우 그 중 하나만 출력하면 된다.
input = sys.stdin.readline

N = int(input())  # 지점의 개수
M = int(input())  # 도로의 개수

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))

def dijkstra(start):
    queue = [(0, start, [start])]
    distance = [0] * (N + 1)
    distance[start] = 0

    while queue:
        dist, now, path = heapq.heappop(queue)
        # print(dist,now, path)

        if now == 1 and len(path) > 1:
            # print("now",now)
            # print("dist", dist)
            # print("distance", distance[start])
            if dist > distance[start]:
                # print("dist", dist)
                distance[start] = dist
            continue

        for next_node, weight in graph[now]:
            new_dist = dist + weight
            if new_dist > distance[next_node]:
                distance[next_node] = new_dist
                new_path = path + [next_node]
                heapq.heappush(queue, (new_dist, next_node, new_path))

    return path, distance[start]

path, max_score = dijkstra(1)

print(max_score)
print(*path)


# N = int(input())  # 지점의 개수
# M = int(input())  # 도로의 개수

# graph = [[] for _ in range(N + 1)]
# for _ in range(M):
#     p, q, r = map(int, input().split())
#     graph[p].append((q, r))

# def dijkstra(start):
#     queue = [(-0, start, [start])]
#     distance = [-float('inf')] * (N + 1)
#     distance[start] = 0
#     best_path = []

#     while queue:
#         dist, now, path = heapq.heappop(queue)
#         dist = -dist
#         print("path",path)

#         if dist < distance[now]:
#             continue

#         if now == 1 and len(path) > 1:
#             print("now",now)
#             print("dist", dist)
#             print("distance", distance[start])
#             if dist == distance[start]:
#                 distance[start] = dist
#                 best_path = path
#             continue

#         for next_node, weight in graph[now]:
#             new_dist = dist + weight
#             if new_dist > distance[next_node]:
#                 distance[next_node] = new_dist
#                 new_path = path + [next_node]
#                 # print(new_path)
#                 heapq.heappush(queue, (-new_dist, next_node, new_path))

#     return best_path, distance[start]

# path, max_score = dijkstra(1)

# print(max_score)
# print(*path)

import sys
from collections import defaultdict, deque

def bellman_ford(graph, n, start):
    # 거리 및 경로 초기화
    dist = [-float('inf')] * (n + 1)
    dist[start] = 0
    prev = [-1] * (n + 1)
    
    # 벨만-포드 알고리즘 수행
    for _ in range(n - 1):
        for u in range(1, n + 1):
            for v, weight in graph[u]:
                if dist[u] + weight > dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u
    
    # 사이클 체크
    for u in range(1, n + 1):
        for v, weight in graph[u]:
            if dist[u] + weight > dist[v]:
                return None, None
    
    return dist, prev

def find_max_score_path(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    
    # 1번 지점에서 벨만-포드 알고리즘 실행
    dist, prev = bellman_ford(graph, n, 1)
    
    if dist is None:
        return "No solution", []

    # 최대 점수 및 경로 찾기
    max_score = -float('inf')
    end_point = -1
    for u in range(1, n + 1):
        if dist[u] > max_score and u != 1:
            for v, weight in graph[u]:
                if v == 1:
                    max_score = dist[u] + weight
                    end_point = u

    # 경로 추적
    path = []
    if end_point != -1:
        node = end_point
        while node != -1:
            path.append(node)
            node = prev[node]
        path.append(1)
        path.reverse()

    return max_score, path

# 입력 받기
n = int(input().strip())
m = int(input().strip())
edges = []
for _ in range(m):
    p, q, r = map(int, input().strip().split())
    edges.append((p, q, r))

# 최대 점수 경로 찾기
max_score, path = find_max_score_path(n, edges)

# 결과 출력
print(max_score)
print(" ".join(map(str, path)))
