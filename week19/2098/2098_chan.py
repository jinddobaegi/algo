import sys
sys.stdin = open("week19/2098/2098.txt")
input = sys.stdin.readline

# cities = int(input())
# cost = [list(map(int, input().split())) for _ in range(cities)]
# min_cost = 99999999999

# def dfs(start,count,total_cost,first):
#     global min_cost
#     if count == cities:
#         if cost[start][first] > 0:  # 출발지로 돌아올 수 있는 경로가 있는 경우에만
#             min_cost = min(min_cost, total_cost + cost[start][first])
#         return
#     for goal in range(cities):
#         if visited[goal] and cost[start][goal] > 0:
#             visited[goal] = False
#             dfs(goal,count + 1,total_cost + cost[start][goal],first)
#             visited[goal] = True
#         else:
#             continue

    
# for i in range(cities):
#     visited = [True]*cities
#     visited[i] = False
#     dfs(i, 1, 0, i)

# print(min_cost)