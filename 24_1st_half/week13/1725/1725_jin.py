N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

for i in range(N):













# 실패...

# from collections import deque
#
# # N: 1 ~ 10만
# # a ~ b범위의 사각형 중, 높이가 가장 낮은 것이 높이가 됨
# # 범위를 지정하고, 그 중 가장 낮은 높이를 찾으면 됨
# # 시작점과 끝점을 어떻게 정할지?
# # 끝점만 늘렸을 때와, 끝점과 시작점을 늘렸을 때의 넓이를 비교하면 되지 않을까?
#
# # 시작, 끝점의 높이만 봤더니 이렇게 하니까 중간에 있는 최소 높이를 못 구함
#
# # 범위 내의 최소 높이만 잘 갱신해주면 될 것 같은데
# # 큐 사용?
# # 끝에 막대 하나 추가했을 때 넓이랑
# # 맨 앞 막대 하나 뺐을 때 넓이 비교해보자
#
# N = int(input())
#
# max_v = 0
# q = deque()
# for i in range(N):
#     h = int(input())  # 0이 있을 수 있음!
#
#     q.append((i, h))
#
#     h1 = min(tuple(map(lambda x: x[1], q)))
#
#     q_len = len(q)
#
#     # 1) 하나 추가만 된 상태
#     area1 = q_len * h1
#
#     # 2) 앞에꺼 하나 뺀 상태(q 길이 2 이상일 때만)
#     if q_len < 2:
#         continue
#
#     head = q.popleft()
#     h2 = min(tuple(map(lambda x: x[1], q)))
#     area2 = (q_len-1) * h2
#
#     tmp_area = 0
#     is_area_1 = True
#
#     # 두 개 중에 큰 거를 판단
#     if area1 < area2:
#         tmp_area = area2
#         is_area_1 = False
#     else:
#         tmp_area = area1
#
#     if max_v < tmp_area:
#         max_v = tmp_area
#         if is_area_1:
#             q.appendleft(head)
#
# print(max_v)