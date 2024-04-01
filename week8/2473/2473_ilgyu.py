
import sys
sys.stdin = open('input.txt')
from itertools import combinations
#
# N = int(input())
# liquor = list(map(int, input().split()))
# print(liquor)

# 조합으로 하는 경우 시간 복잡도가 O(N^3) N개중 3개 요소 선택이니까 => 투 포인터로 해야함

# min_dif = 3000000000 # 0과의 차이 최소값 / 초기를 그냥 3억으로 설정
# ans_list = []
# for combo in combinations(liquor, 3):
#     cur_sum = sum(combo)
#     if abs(cur_sum - 0) < min_dif:  # 현재 조합의 합과 목표값(N)과의 차이가 이전 최소값보다 작으면
#         min_dif = abs(cur_sum - 0)  # 최소 차이 업데이트
#         ans_list = combo
#
# ans = sorted(ans_list)
# # print(ans)
# # print(min_dif)
# output = ' '.join(str(x) for x in ans)
# print(output)


# 투 포인터 기본 코드
# n = 5 # 데이터의 개수 N
# m = 5 # 찾고자 하는 부분합 M
# data = [1, 2, 3, 2, 5] # 전체 수열
#
# count = 0
# interval_sum = 0
# end = 0
#
# # start를 차례대로 증가시키며 반복
# for start in range(n):
#     # end를 가능한 만큼 이동시키기
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     # 부분합이 m일 때 카운트 증가
#     if interval_sum == m:
#         count += 1
#     interval_sum -= data[start]
#
# print(count)

# 리스트를 정렬해서 하나 잡고 나머지 두개를 이분탐색?
# liquor.sort()
# print(liquor)

# 합이 0에 가장 가까운 리스트를 기록해야할듯
# closest_sum = 3000000000
# # [-97, -6, -2, 6, 98]
# for point in range(N):

n = int(input())
array = list(map(int, input().split()))

array.sort()
minTake = sys.maxsize

for i in range(n - 2): # 세개를 선택할거니까 끝에서 3개 선택하는경우 고려해서 n-2까지만 i를 돌아
    start = i + 1
    end = n - 1
    while start < end:
        take = array[i] + array[start] + array[end]
        if abs(take) < minTake:
            minTake = abs(take)
            result = [array[i], array[start], array[end]]
        if take < 0: # 세수의 합이 0보다 적으면 start를 오른쪽으로 이동시켜 합을 증가시킴
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])