import sys
sys.stdin = open('input.txt')
import copy

n = int(input()) # 이동하려고하는 채널
m = int(input()) # 고장난 버튼 수
if m > 0:
    broken = list(map(int, input().split())) # 고장난 버튼들
else:
    broken = []

ans = abs(n - 100)
for ch in range(0, 1000001):
    temp = str(ch)

    for x in temp:
        if int(x) in broken:
            break
    else:
        ans = min(ans, len(temp) + abs(n - ch))

print(ans)




#
# target = str(n)
# # print(target)
#
# # 1. 현재 내가 누를 수 있는 버튼들로 가장 근접한 수를 누른 후에
# # 가장 근접한 수를 어떻게 선택할거냐
# # 2. +, - 로 이동하는 거
# my_num = ""
# head = 0
# first = int(target[0])
# dif = 10
# # 1. 맨 앞 숫자를 결정
# for num in button:
#     temp = abs(num - first)
#     if temp < dif:
#         dif = temp
#         head = num
#
# # print(head)
# my_num += str(head * (10**(len(target)-1)))
# # print(my_num)
#
# # 이제 2번째 수부터 뭘 선택할지 결정할거임
# # 어떻게 결정하냐
# # button의 수를 하나씩 선택해서
# # 71000, 72000, 73000... 이런 수를 만들어서
# # 만들 수 있는 수와 target과의 차이가 가장 작은 수를 선택해서 my_num의 2번째 숫자로 해주는겨
# number_lst = list(my_num)
#
# for i in range(1, len(target)):
#     temp = float('inf') # n과 내가 만든 임의의 수의 차이
#     res = 0
#     for num in button:
#         num_lst = copy.deepcopy(number_lst)
#         num_lst[i] = num # 특정 위치의 숫자를 바꾸고 (이건 리스트)
#         # print(number_lst)
#         # print(num_lst)
#         # 얘를 다시 합쳐서
#         ths_str = ''.join(map(str, num_lst))
#         # print(num_lst)
#         # 다시 숫자로 바꿔주고
#         ths_num = int(ths_str) # 여기까지 하면 71000같은 숫자가 만들어짐
#         # print(ths_num)
#         # print(temp)
#         print(n)
#         if abs(n - ths_num) < temp: # 만약 이 차이가 더 작으면
#             res = num
#             temp = abs(n - ths_num)
#     number_lst[i] = res
#
#
# print(number_lst) # 예제 1번 5455가 나와야 하는데
# semi_ans = ""
# for x in number_lst:
#     cur = str(x)
#     semi_ans += cur
# # print(semi_ans)
# my_target = int(semi_ans)
# ans = abs(n - my_target) + len(semi_ans)
# # print(ans)