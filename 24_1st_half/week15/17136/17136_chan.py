import sys
sys.stdin = open("week15/17136/17136.txt")
input = sys.stdin.readline
from collections import deque

# graph = [list(map(int, input().split())) for _ in range(10)]

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
# 색종이는 5장씩 있으며 정사각형이고 1 부터 5까지이다.
# 1이 적힌 모든 칸을 색종이로 채우는데 필요한 색종이의 최소개수 카운트 / 불가능한 경우 -1을 출력

graph = [list(map(int , input().split())) for _ in range(10)]
# for i in graph:
#     print(i)
paper = [5,5,5,5,5,5]
min_count = 1000

def true_false_paper(x, y, size):
    if x + size > 10 or y + size > 10: #범위 안에 있는지 확인
        return False
    for i in range(size):
        for j in range(size):
            if graph[x + i][y + j] != 1: # 범위안에 있는데 1이 아닌게 있으면 False
                return False
    return True # 나비머지의 경우에는 트루

def input_paper(x, y, size, value): #종이 추가 밑 제거가능
    for i in range(size):
        for j in range(size):
            graph[x + i][y + j] = value


def dfs(x, y, count):
    global min_count
    if x == 10: # 10이 되면 종료한다.
        min_count = min(min_count, count)
        return
    
    if y == 10: # y열 먼저 검사하고 10이되면 다음으로 넘어간다 
        dfs(x + 1, 0, count)
        return
    
    if graph[x][y] == 1: #1인경우
        for size in range(5, 0, -1):
            if paper[size] > 0 and true_false_paper(x, y, size): 
                input_paper(x, y, size, 0) # 종이 추가
                paper[size] -= 1
                dfs(x, y + 1, count + 1)
                input_paper(x, y, size, 1) # 종이 제거(초기화)
                paper[size] += 1 #초기화
    
    else: # 아닌경우 
        dfs(x, y + 1, count)

dfs(0, 0, 0)

print(min_count if min_count != 1000 else -1)