from sys import stdin

input = stdin.readline

N = int(input())  # 3 ~ 5000
arr = list(map(int, input().split()))  # -10억 ~ 10억
arr.sort()

# 절댓값이 가장 작은 쪽으로 갱신(값으로 확인하고 용액들 갱신)
min_v = int(1e9 * 3)
isFound = False
res = []

# 검색했습니다...
for i in range(N-2):
    if isFound:
        break
    refer = arr[i]
    l_p = i+1
    r_p = N-1
    while l_p < r_p:
        tmp = refer + arr[l_p] + arr[r_p]
        if min_v > abs(tmp):
            min_v = abs(tmp)
        '''
        위 코드처럼 하면 abs 한 번 하고
        if에 해당하면 abs 한 번 더하는데
        
        아래 코드는 무조건 abs를 두 번 해서
        시간 초과가 뜸
        if abs(min_v) > abs(tmp): 
            min_v = tmp
        '''
            res = [refer, arr[l_p], arr[r_p]]
        if tmp < 0:
            l_p += 1
        elif tmp > 0:
            r_p -= 1
        else:
            isFound = True
            break

print(*res)


# 아래 방법은 실패....

# 타겟값 혹은 타겟 근삿값 찾는 함수
# def bin_search(s, e, target):
#     while s <= e:
#         m = (s+e) // 2
#         if arr[m] == target:
#             return target
#
#         else:
#             if arr[m] > target:
#                 e = m-1
#             else:
#                 s = m+1
#
#     return arr[s]
#
#
# def find_liquid(l, r):
#     global min_v, res
#
#     while l < r:
#         left = arr[l]
#         right = arr[r]
#         mid = -(left + right)
#
#         # 합이 0이 되는 경우
#         if mid in arr:
#             res = [left, right, mid]
#             return
#
#         # 0이 안되는 경우
#         # -> 최대 근사치를 찾아보자
#         nearest_mid = bin_search(l, r, mid)
#
#         gap = mid + nearest_mid
#         tmp_total = left + right + nearest_mid
#
#         # 최솟값 갱신
#         if min_v > tmp_total:
#             min_v = tmp_total
#             res = [left, right, nearest_mid]
#
#         # l, r 이동
#         if arr[l+1] - arr[l] < arr[r] - arr[r-1]:
#             l += 1
#         else:
#             r -= 1
#
#
# find_liquid(0, N-1)
# res.sort()
#
# print(res)