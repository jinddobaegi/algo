N = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

cnt = 0
start = 0
end = N-1

# 투포인터
# 합이 x보다 작은 경우 -> 더 큰 값 더하도록 start += 1
# 합이 x보다 큰 경우 -> 더 작은 값 더하도록 end -= 1
while start < end:
    n_sum = arr[start] + arr[end]

    if n_sum == x:
        cnt += 1
        start += 1
    elif n_sum < x:
        start += 1
    else:
        end -= 1

print(cnt)


# 시간초과
# for i in range(N-1):
#     for j in range(i+1, N):
#         n_sum = arr[i] + arr[j]
#
#         if n_sum == x:
#             cnt += 1