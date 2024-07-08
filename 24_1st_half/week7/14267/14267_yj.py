import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * (N+1)
temp = list(map(int, input(). split()))

# 직속 상사의 칭찬 + 본인 칭찬으로 계산?
# 일단 본인이 받은 칭찬 더하기
for _ in range(M):
    i, w = map(int, input().split())
    arr[i] += w

# 직속 상사가 받은 칭찬 더하기
for i in range(2, N+1):
    arr[i] += arr[temp[i-1]]

ans = ' '.join(map(str, arr[1:N+1]))
print(ans)




# 당연하게도 시간 초과
# 그냥 시도해봄^^..
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# arr = [0] * (N+1)
# temp = list(map(int, input().split()))
#
# for _ in range(M):
#     i, w = map(int, input().split())
#
#     for j in range(i, N+1):
#         arr[j] += w
#
# ans = ' '.join(map(str, arr[1:N+1]))
# print(ans)