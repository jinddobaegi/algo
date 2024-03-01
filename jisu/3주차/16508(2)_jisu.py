# 전공책
# 순열로 풀어보겠어.

# lst = [1, 2, 3]
# N = len(lst)
#
# # nPr  depth = r
# def permutation(arr, depth, visit):
#     if (depth == N): # 종료조건
#         print(arr)
#         return
#
#     for idx in range(N):
#         if (visit[idx]):
#             continue
#         visit[idx] = 1
#         arr[depth] = lst[idx]
#         permutation(arr, depth + 1, visit)
#         visit[idx] = 0
#
# arr = [0 for _ in range(N)]
# visit = [0 for _ in range(N)]
# permutation(arr, 0, visit)

T = input() # 만들어야 하는 문자열
N = int(input())
books = list(list(map(int, input().split())) for _ in range(N))
