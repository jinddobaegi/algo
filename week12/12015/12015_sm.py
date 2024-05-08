# 가장 긴 증가하는 부분 수열 2
# 골드2

# 오.. 수열...

# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에
# 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 이진탐색 슈웃 -

import sys
input = sys.stdin.readline

def binarySearch(target, start, end):
    while start<= end:
        mid = (start + end) // 2

        if stack[mid] < target:
            start = mid +1
        else:
            end = mid - 1

    return start  # target 값이 들어갈 위치 반환

N = int(input())
A = list(map(int, input().split()))
# 일단 스택을 초기화하고
stack = [0]

# 입력받은 수열 돌면서
for i in A:
    # 현재값이 스택 마지막 값보다 크면 추가
    if stack[-1] < i:
        stack.append(i)
    else:
        # 아니면 이진탐색으로 위치 찾아서 그 값으로 바꿔
        stack[binarySearch(i, 0, len(stack)-1)] = i

# 초기값 뺀 길이 출력
print(len(stack) -1)

