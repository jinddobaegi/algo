import sys
sys.stdin = open("week32/1107/1107.txt")

N = int(input())  # 목표 채널
M = int(input())  # 사용할 수 없는 버튼의 개수

if M > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

remote_num = [i for i in range(10) if i not in broken_buttons]

min_push = abs(N-100)

for num in range(1000000):
    num_str = str(num)

    for digit in num_str:
        if int(digit) not in remote_num:
            break
    else:
        min_push = min(min_push, len(num_str) + abs(num-N))

print(min_push)


# # 고장난 버튼이 있는 경우 입력받기
# if M > 0:
#     remote__delete_num = list(map(int, input().split()))
# else:
#     remote__delete_num = []

# # 사용할 수 있는 버튼 목록 생성
# remote_num = [i for i in range(10) if i not in remote__delete_num]

# def cal(K):
#     target_digits = [int(i) for i in str(K)]  # 목표 숫자를 자릿수로 나누기
#     result_digits = []
    
#     for i, digit in enumerate(target_digits):
#         if digit in remote_num:
#             result_digits.append(digit)
#         else:
#             # 현재 자릿수보다 큰 값과 작은 값 찾기
#             plus_num = min([num for num in remote_num if num > digit], default=None)
#             minus_num = max([num for num in remote_num if num < digit], default=None)
            
#             # 가장 가까운 값 선택
#             if plus_num is not None and minus_num is not None:
#                 if abs(plus_num - digit) < abs(minus_num - digit):
#                     result_digits.append(plus_num)
#                     # 남은 자릿수를 최소 값으로 채움
#                     result_digits.extend([min(remote_num)] * (len(target_digits) - len(result_digits)))
#                 else:
#                     result_digits.append(minus_num)
#                     # 남은 자릿수를 최대 값으로 채움
#                     result_digits.extend([max(remote_num)] * (len(target_digits) - len(result_digits)))
#             elif plus_num is not None:
#                 result_digits.append(plus_num)
#                 result_digits.extend([min(remote_num)] * (len(target_digits) - len(result_digits)))
#             elif minus_num is not None:
#                 result_digits.append(minus_num)
#                 result_digits.extend([max(remote_num)] * (len(target_digits) - len(result_digits)))
#             break
    
#     # 자릿수를 합쳐 숫자로 변환
#     result = int(''.join(map(str, result_digits)))
    
#     # 숫자 버튼으로 이동한 경우와 +/- 버튼으로 이동한 경우 중 최소값 반환
#     return min(len(result_digits) + abs(result - N), abs(N - 100))

# # 최종 결과 출력
# print(cal(N))