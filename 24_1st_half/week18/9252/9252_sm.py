# LCS 2
# 골드4

# 문제
'''
LCS(최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
'''

# 풀이법
'''
- 문자가 일치하면 이전 문자까지의 길이에 1 더해
- 불일치하면 이전의 최댓값으로 유지
- 2차원 배열 역추적해서 실제 lcs 문자열을 출력해주는 것
'''

import sys
input = sys.stdin.readline

# 처음에 그냥 input으로 써서 틀림
# input().rstrip()을 써서 오른쪽 공백 제거하니까 통과됨
first = input().rstrip()
second = input().rstrip()


n = len(first) # 첫번째 문자 길이
m = len(second) # 두번째 문자 길이

# 두 문자열의 최장 공통 부분 문자열 길이 저장해주는 2차원 리스트
lst = [[0] * (n + 1) for _ in range(m + 1)]

# 2중으로 돌면서
for i in range(1, m + 1):
    for j in range(1, n + 1):

        # 현재 위치 문자가 일치하면 대각선 위 값에 +1
        if first[j - 1] == second[i - 1]:
            lst[i][j] = lst[i - 1][j - 1] + 1


        # 불일치면 더큰 값을 현재 위치에 저장해
        else:
            lst[i][j] = max(lst[i - 1][j], lst[i][j - 1])


# 마지막값  lcs 길이 출력해
print(lst[m][n])


# lcs  길이가 0이 아닐 때만 실행되게 하자
if lst[m][n] != 0:
    current_x, current_y = m, n

    # 문자열 저장 변수 초기화
    res = ""

    # 역추적 시작 (m, n)
    # 현재 위치가 (0, 0)이 될 때까지 반복
    while current_x != 0 and current_y != 0:
        # 현재 위치의 문자가 같으면
        if first[current_y - 1] == second[current_x - 1]:
            # res에 해당 문자를 추가
            res += first[current_y - 1]
            # 대각선 왼쪽 위로 이동
            current_x -= 1
            current_y -= 1
        # 다르믄
        else:
            if lst[current_x][current_y] == lst[current_x - 1][current_y]:
                current_x -= 1  # 좌로 이동

            elif lst[current_x][current_y] == lst[current_x][current_y - 1]:
                current_y -= 1  #  위로 이동


    # 역순으로 출력
    print(res[::-1])