import sys
sys.stdin = open("week15/17136/17136.txt")
input = sys.stdin.readline
from collections import deque

graph = [list(map(int, input().split())) for _ in range(10)]

# 첫시도
# visited = [[0] * 10 for _ in range(10)]

# def check_area(x, y):
#     stack = deque([(x, y)])
#     count = 1
#     while stack:
#         if count == 5:
#             break
#         x, y = stack.popleft()
#         delta = ((0, 1), (1, 0))
#         for dx, dy in delta:
#             rnx, rny = x + dx[0], y + dx[1]
#             dnx, dny = x + dy[0], y + dy[1]
#             if 0 <= rnx < 10 and 0 <= rny < 10 and 0 <= dnx < 10 and 0 <= dny < 10:
#                 if graph[rnx][rny] == 1 and graph[dnx][dny] == 1:



# 두번째 시도
# def check_area_size(x, y): #가로의 길이를 먼저 재고
#     count = 1
#     for i in range(1, 5):
#         if graph[x][y + i] == 1:
#             count += 1
#         else:
#             break
#     return count


# def check_area(x, y):
#     length = check_area_size(x, y)  # 가로의 길이를 잰다.
#     stack = deque([length])  # 가로의 길이를 스택에 넣는다.
#     check = False
#     while stack:
#         size = stack.popleft()
        
#         if check or size == 1:  # 체크가 True이면 정사각형을 0으로 바꾸고 1을 리턴한다.
#             # print("size = ",size)
#             for row in range(size):
#                 for col in range(size):
#                     graph[x + row][y + col] = 0
#             check_list[size-1] -= 1
#             if check_list[size-1] < 0:
#                 return 100
#             else:
#                 return 1
#         else:
#             valid = True
#             # print("size2 = ",size)
#             for row in range(size):
#                 for col in range(size):
#                     if x + row >= 10 or y + col >= 10 or graph[x + row][y + col] == 0:  # 0이 하나라도 나오면
#                         stack.append(size - 1)  # 사이즈 -1을 하여 스택에 다시 넣는다.
#                         valid = False
#                         break
#                 if not valid:
#                     break
#             if valid:
#                 stack.append(size)
#                 check = True
#             else:
#                 stack.append(size - 1)  # size를 다시 스택에 넣지 않으면 size가 계속 감소하지 않습니다.


# check_list = [5,5,5,5,5]
            
# result = 0
# for row in range(10):
#     for col in range(10):
#         if graph[row][col] == 0:
#             continue
#         # print(check_area(row, col))
#         result += check_area(row, col)
#         print(check_list)
#         # for i in graph:
#         #     print(i)
#         # print("------------------------------------")

# if result >= 100:
#     print(-1)
# else:
#     print(result)



# 세번째 시도