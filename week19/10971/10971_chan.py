# import sys
# sys.stdin = open("week19/10971/10971.txt")

# 외판원 순회2

# 외판원 순회 문는 영어로 Traveling Salesman problem (TSP)라고 불리는 문제로 
# computer science 분야에서 가장 중요하게 취급되는 문제중 하나이다.
# 여러가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.
# 1번부터 N번 까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.(길이 없을 수도 있다.)
# 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 
# 다시 원래의 도시로 돌아오는 수니회 여행 경로를 계획히려고 한다. 단, 한번 갔던 도시로는 다시 갈 수 없다.(맨 마지막에 여행을 출발했던 도시로 돌아오는것은 예외)
# 이런 여행 경로는 여러가지가 있을 수 있는데, 가장 적은 비용을 들이는 여행 계획을 세우고자 한다. 
# 각 도시 간에 이동하는데 디는 비용은 행렬 W[i][j]형태로 주어진다.
# W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
# 비용은 대칭적이지 않다. 즉, W[i][j]는 W[j][i]와 다를 수 있다. 
# 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다.
# 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 이씅며 이럴 경우 W[i][j]=0이라고 하자.


#2차원배열은 비대칭이다.(오고가고 비용이다름)
#N개의 도시를 모두 거쳐 다시 출발했던 도시로 돌아와야 한다.
#출발도시는 랜덤이고 한번들린도시는 다시 들릴 수 없다.
# 최소 비용을 구하자

import sys
sys.stdin = open("week19/10971/10971.txt")
input = sys.stdin.readline

cities = int(input())
cost = [list(map(int, input().split())) for _ in range(cities)]
min_cost = 99999999999

def dfs(start,count,total_cost,first):
    global min_cost
    if count == cities:
        if cost[start][first] > 0:  # 출발지로 돌아올 수 있는 경로가 있는 경우에만
            min_cost = min(min_cost, total_cost + cost[start][first])
        return
    for goal in range(cities):
        if visited[goal] and cost[start][goal] > 0:
            visited[goal] = False
            dfs(goal,count + 1,total_cost + cost[start][goal],first)
            visited[goal] = True
        else:
            continue

    
for i in range(cities):
    visited = [True]*cities
    visited[i] = False
    dfs(i, 1, 0, i)

print(min_cost)
