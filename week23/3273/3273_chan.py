import sys
sys.stdin = open("week23/3273/3273.txt")


N = int(input())
sequence = list(map(int, input().split()))
x = int(input())

# 시간초과 N의 제곱이라서
# graph = []
# count = 0
# for i in range(N):
#     for j in range(i+1, N):
#         # if sequence[i] < sequence[j]:
#         if sequence[i] + sequence[j] == x:
#             a = sequence[i]
#             b = sequence[j]
#             graph.append((a, b))
#             count += 1
            
# # print(sequence)
# # print(graph)
# print(count)

# 투포인터
# count = 0
# interval_sum = 0
# end = 0

# for start in range(N):
#     while interval_sum < x and end < N:
#         interval_sum += sequence[end]
#         end += 1
#     if interval_sum == x:
#         count += 1
#     interval_sum -= sequence[start]

# print(count)

#투포인터
sequence.sort()
left = 0
right = N - 1
init_sum = 0

while left < right:
    tmp_sum = sequence[left] + sequence[right]
    if tmp_sum == x:
        init_sum += 1
        left += 1
        right -= 1
    elif tmp_sum < x:
        left += 1
    else:
        right -= 1

print(init_sum)

        







