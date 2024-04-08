# 1931
# 실버1

# 문제
# N개의 회의
# start = end이면 시작하자마자 끝나는 것
# 회의 중단 불가능 / 끝남과 동시에 다음 회의 시작 가능


# 전략
# 최대한 많은 회의 개수를 뽑아내려면 가장 이른 시간부터 선택해야겠지 -> 근데 회의시간 길면 말짱도루굼
# 회의시간 짧은 것들을 선택 -> 시작/끝 시간 모를듯 , 시간이 뒤죽박죽됨
# 종료시간 기준 빠른거 선택!

import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())

time = []  # 시간을 담을 리스트
for _ in range(N):
    # 회의 시작시간, 종료 시간
    start, end = map(int, sys.stdin.readline().split())
    time.append((start, end))

# 끝나는 시간을 기준으로 sort
time.sort(key=lambda x : (x[1], x[0]))
# print(time)
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# 회의 최대 개수 : 적어도 회의는 무조건 하나 이상)
cnt = 1

# 처음 회의가 끝난 시간
end = time[0][1]   # 4

# 반복문 돌면서 앞선 end값보다 시작값이 커야지만 할 수 있게 ㄱ
for i in range(1, N):  # 근데 값은 2번째부터 비교해야하니까 범위 조심하긔
    if time[i][0] >= end:
        end = time[i][1]
        cnt += 1
# 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의 최대 개수 출력
print(cnt)