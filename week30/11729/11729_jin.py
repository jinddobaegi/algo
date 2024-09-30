from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10**6)

N = int(input())

# 장대는 무조건 세 개
# 항상 위가 아래보다 작아야 함


# 참조자료: https://youtu.be/FYCGV6F1NuY
# 함수의 의미: num개의 원판을 start에서 goal 기둥으로 옮길 것이다. sub는 안 쓰는 기둥
# 함수의 인자: 안 옮긴 원반 개수, 옮기기 전 기둥, 옮긴 뒤 기둥, 나머지 기둥
def solution(num, start, goal, sub):
    # 옮길 원반이 한 개 남으면 print
    if num == 1:
        print(start, goal)
        return

    # 1) 가장 큰 원반 제외하고 N-1개의 원반을 "현재 기둥"에서 모두 "보조 기둥"으로 옮기기
    solution(num-1, start, sub, goal)
    # 2) 시작 기둥에 남은 가장 큰 원반 "현재 기둥" -> "목표 기둥"
    print(start, goal)
    # 3) "보조 기둥"에 옮겨놓은 n-1개의 원반들 "목표 기둥"으로 옮기기
    solution(num-1, sub, goal, start)


print(2**N-1)  # 규칙에 의한 개수
solution(N, 1, 3, 2)


# 실패 코드

# A = [x for x in range(N, 0, -1)]
# arr = [[x for x in range(N, 0, -1)], [], []]
# visited = [[], []]  # 두 개 장대의 상태만 확인해보자


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
#
#
# min_v = int(1e9)
# solution(0)
# print(min_v)