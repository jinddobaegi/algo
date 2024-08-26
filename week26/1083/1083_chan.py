import sys
sys.stdin = open("week26/1083/1083.txt")
input = sys.stdin.readline

# def cal(S):
#     count = S
#     while count > 0:
#         for i in range(N-1):
#             if number_list[i] < number_list[i+1]:
#                 number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
#                 count -= 1

# N = int(input())
# number_list = list(map(int, input().split()))
# S = int(input())

# cal(S)

# print(number_list)


def cal(N, A, S):
    for i in range(N):
        if S == 0:
            break

        max_pos = i
        for j in range(i + 1, min(i + 1 + S, N)):
            if A[j] > A[max_pos]:
                max_pos = j

        for k in range(max_pos, i, -1):
            A[k], A[k - 1] = A[k - 1], A[k]
            S -= 1 
            if S == 0:
                break

    return A

N = int(input())
number_list = list(map(int, input().split()))
S = int(input())

result = cal(N, number_list, S)

print(*result)