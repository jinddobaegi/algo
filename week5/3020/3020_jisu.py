# 개똥벌레
# import bisect

# 배열이 정렬되어있으니까 [1, 3, 5]의 높이를 가지고 있는 석순 혹은 종유석이라면
# 타겟이 부딪히는 지점을 찾고 난 이후에는 찾을 필요가 없음.
# start가 (종유석/석순) index니까 start리턴
def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

N, H = map(int, input().split()) # N: 동굴의 길이, H: 높이. N은 항상 짝수

bottom = [] #석순
top = [] # 종유석
for i in range(N):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

# 이진 탐색은 정렬이 필수
bottom.sort()
top.sort()

min_c = N #최소 카운트
cnt = 0 #몇 번?

for i in range(1, H + 1):
    # b_cnt = binary(bottom, i - 0.5, 1, N // 2) # start가 인덱스니까
    # t_cnt = binary(top, H - i + 0.5, 1, N // 2) # start끼리 더하면 될 줄 알았는데 인덱싱 에러 ㅠㅠ
    b_cnt = (N//2) - binary(bottom, i - 0.5, 0, (N//2) - 1)
    t_cnt = (N//2) - binary(top, H - i + 0.5, 0, (N//2) - 1)

    if min_c == b_cnt + t_cnt:
        cnt += 1
    elif min_c > b_cnt + t_cnt: # 현재 범위가 새로운 최소 값이면
        cnt = 1
        min_c = b_cnt + t_cnt

print(min_c, cnt)


# 메모리 초과
# N, H = map(int, input().split()) # N: 동굴의 길이, H: 높이. N은 항상 짝수
# cave = [[] for _ in range(N)]
#
# # 석순이랑 종유석 동굴 리스트에 저장
# for i in range(N//2):
#     for a in range(1, int(input()) + 1):
#         cave[i*2].append(a)
#     for b in range(int(input())):
#         cave[i*2+1].append(H - b)
#
# # print(cave) # [[1], [7, 6, 5, 4, 3], [1, 2, 3], [7, 6, 5], [1, 2, 3, 4, 5], [7]]
# min_v = N
# counting = 1
# for i in range(1, H + 1):
#     cnt = 0
#     for j in range(N):
#         cnt += cave[j].count(i)
#     if min_v == cnt:
#         counting += 1
#     elif cnt < min_v:
#         min_v = cnt
#         counting = 1
#
# print(min_v, counting)