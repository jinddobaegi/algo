from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**8)

N = int(input())
A = [x for x in range(N, 0, -1)]

# 장대는 무조건 세 개
# 항상 위가 아래보다 작아야 함

arr = [[x for x in range(N, 0, -1)], [], []]
# visited = [[], []]  # 두 개 장대의 상태만 확인해보자


# 실패 코드
# def solution(cnt):
#     global min_v
# 
#     if arr[2] == A:
#         min_v = min(min_v, cnt)
#         return
# 
#     for i in range(3):
#         for j in range(3):
#             if i == j:
#                 continue
#             if arr[i]:
#                 if not arr[j] or arr[i] < arr[j]:
#                     print(arr)
#                     x = arr[i].pop()
#                     arr[j].append(x)
# 
#                     if arr[0] not in visited[0] and arr[1] not in visited[1]:
#                         visited[0].append(arr[0])
#                         visited[1].append(arr[1])
#                         solution(cnt + 1)
#                         visited[0].pop()
#                         visited[1].pop()
# 
#                     x = arr[j].pop()
#                     arr[i].append(x)


min_v = int(1e9)
solution(0)
print(min_v)