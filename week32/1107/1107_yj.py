import sys
input = sys.stdin.readline
N = int(input()) # 이동하려고 하는 채널
M = int(input()) # 고장난 버튼의 개수
buttons = list(map(int, input().split())) # 고장난 버튼

# 모든 경우의 수 탐색
# 고장나지 않은 숫자들로 만들 수 있는 순열 만들기 -> 가려고 하는 채널과 가까운 순열을 찾아서 차이를 구해보자

min_cnt = abs(100 - N)  # +나 - 버튼만으로 이동하는 경우

for num in range(1000001):
    for j in str(num):
        if int(j) in buttons:
            break

    else:
        min_cnt = min(min_cnt, abs(num - N) + len(str(num)))

print(min_cnt)