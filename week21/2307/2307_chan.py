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

def check1(start):
    distance[start] = 0 
    queue = ([0, start]) # 거리, 노드

    while queue:
        c_dist, c_node = heapq.heappop(queue)

        if c_dist > distance[c_node]:
            continue

        for goal in range(nodes + 1):
            if graph[c_node][goal] != float('inf'):
                distance_to_goal = c_dist + graph[c_node][goal]

                # 더 짧은 경로를 발견한 경우
                if distance_to_goal < distance[goal]:
                    print(distance[goal])
                    distance[goal] = distance_to_goal
                    heapq.heappush(queue, (distance_to_goal, goal))




nodes, loads = map(int, input().split())
distance = [0] * (loads + 1)

graph = [[0] * (nodes + 1) for _ in range(loads)]

for _ in range(loads):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t

check1(0)
