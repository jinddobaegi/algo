# import sys
# sys.stdin = open('input.txt')
#
# def dfs(num):
#     global cnt
#     for k in range(1, N+1):
#         if adj_arr[num][k] == 1:
#             cnt += 1
#             dfs(k)
#
# N, M = map(int, input().split())
# adj_arr = [[0] * (N+1) for _ in range(N+1)]
#
# for _ in range(M):
#     s, e = map(int, input().split())
#     adj_arr[e][s] = 1
# # print(adj_arr)
#
# ans_list = []
# for i in range(1, N+1):
#     cnt = 0
#     dfs(i)
#     ans_list.append([i, cnt])
#
# max_value = 0
# for case in ans_list:
#     max_value = max(case[1], max_value)
#
# real_ans = []
# for case in ans_list:
#     if case[1] == max_value:
#         real_ans.append(case[0])
#
# real_ans.sort()
# print(" ".join(map(str, real_ans)))
# 메모리 초과 => adj_arr 방식이 메모리를 많이 잡아먹나봄


import sys
sys.stdin = open('input.txt')

def dfs(num):
    global cnt
    stack = [num]
    visited = [False] * (N+1)
    visited[num] = True

    while stack:
        cur = stack.pop()
        for com in adj_arr[cur]:
            if visited[com] == False:
                visited[com] = True
                cnt += 1
                stack.append(com)


N, M = map(int, input().split())
adj_arr = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_arr[e].append(s)
# print(adj_arr)

ans_list = []
for i in range(1, N+1):
    cnt = 0
    dfs(i)
    ans_list.append([i, cnt])

max_value = 0
for case in ans_list:
    max_value = max(case[1], max_value)

real_ans = []
for case in ans_list:
    if case[1] == max_value:
        real_ans.append(case[0])

real_ans.sort()
print(" ".join(map(str, real_ans)))
# 메모리 초과 => adj_arr 방식이 메모리를 많이 잡아먹나봄




