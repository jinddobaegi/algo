# 첫 줄에는 지점의 수를 나타내는 정수 N(6 ≤ N ≤ 1000)과 도로의 수 M(6 ≤ M ≤ 5000)이 주어진다.
# 그 다음 이어 나오는 M개의 각 줄에는 도로(a, b)와 그 통과시간 t가 a b t 로 표시된다. 단 이 경우 a < b 이고 1 ≤ t ≤ 10000이다.

# 출력
# 경찰이 하나의 도로를 막음으로써 지연시킬 수 있는 최대 시간을 정수로 출력한다. (단, 그 지연시간이 무한대이면 -1을 출력해야 한다.)

# 지연시간을 고르는 것이니까 
# 최소시간을 다익스트라를 이용해서 구하고
# 경로또한구하고... 각 노드에 검문소를 세운다.
# 검문소가 세워진 도로는 가장큰값을 넣고
# 다시 다익스트라를 이용해서 각각의 최소시간을 구하고
# 그중 가장 큰값을 가지고있는 시간과 처음의 최소시간의 차를 결과값으로 출력한다.

# 최소경로를 찾고 
# 경로의 노드값을 이용해서 각 노드를 검문소로 채택 및 도로를 아주 큰값을 넣기
# 가장 큰값을 가지게 되는 최소경로의 시간과 처음의 최소시간의 차를...! 출력

import sys
sys.stdin = open("week21/2307/2307.txt")
import heapq
input = sys.stdin.readline


# 시간초과
# def djikstra(start):
#     queue = heapq
#     queue = [(0, start)]
#     distance[start] = 0

#     while queue:
#         dist, now = heapq.heappop(queue)

#         if dist > distance[now]:
#             continue
        
#         for next in range(1, N+1):
#             if graph[now][next] != float("INF"):
#                 tmp_dist = dist + graph[now][next]

#                 if tmp_dist < distance[next]:
#                     distance[next] = tmp_dist
#                     heapq.heappush(queue, (tmp_dist, next))
#                     move_image[next] = now
                    

# N, M = map(int, input().split()) # node의 갯수, 도로의 수
# graph = [[float("INF")] * (N + 1) for _ in range(N+1)]
# distance = [float("INF")] * (N+1)
# move_image = [0] * (N + 1)

# # for _ in graph:
# #     print(_)

# for _ in range(M): #2차원 인접행열에 시간 추가해주기
#     a, b, t = map(int, input().split()) #도로a, b 와 통과 시간 t
#     graph[a][b] = t
#     graph[b][a] = t

# djikstra(1)

# # print(distance[N])
# first = distance[N]
# # print(move_image)

# path = []
# current = N
# while current != 0:
#     path.append(current)
#     current = move_image[current]
# path.reverse()
# # print(path)

# new = len(path)

# result = float("INF")
# delay = -1
# for i in range(new - 1):
#     distance = [float("INF")] * (N+1)
#     a = path[i]
#     b = path[i + 1]
#     original_value = graph[a][b]
#     graph[a][b] = float("INF")
#     graph[b][a] = float("INF")

#     djikstra(1)

#     graph[a][b] = original_value
#     graph[b][a] = original_value

#     if distance[N] == float("INF"):
#         delay = -1
#         break
#     else:
#         delay = max(delay, distance[N] - first)

# print(delay)

def dijkstra(start):
    distance[start] = 0
    queue = [(0, start)]

    while queue:
        dist, now = heapq.heappop(queue)

        if dist > distance[now]:
            continue

        for next, weight in graph[now]:
            tmp_dist = dist + weight

            if tmp_dist < distance[next]:
                distance[next] = tmp_dist
                heapq.heappush(queue, (tmp_dist, next))
                move_image[next] = now

def find_path():
    path = []
    current = N
    while current != 0:
        path.append(current)
        current = move_image[current]
    path.reverse()
    return path


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

# 최초 다익스트라 알고리즘 수행
distance = [float('inf')] * (N + 1)
move_image = [0] * (N + 1)
dijkstra(1)

first = distance[N]

path = find_path()

max_delay = -1
for i in range(len(path) - 1):
    a = path[i]
    b = path[i + 1]

    for j in range(len(graph[a])):
        if graph[a][j][0] == b:
            original_value_a = graph[a][j]
            graph[a][j] = (b, float('inf'))
            break

    for j in range(len(graph[b])):
        if graph[b][j][0] == a:
            original_value_b = graph[b][j]
            graph[b][j] = (a, float('inf'))
            break

    new_distance = [float('inf')] * (N + 1)
    distance = new_distance
    dijkstra(1)



    if distance[N] == float("inf"):
        max_delay = -1
        break
    else:
        max_delay = max(max_delay, distance[N] - first)

print(max_delay)









