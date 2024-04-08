# 1. 종료 시간 순으로 정렬
# 2. 종료 시간이 가장 빠른 활동 선택
# 3. 이전 종료 시간과 다음 시작 시간 계속 비교하며 선택
# for문 돌면서 종료 시간이랑 비교하여 선택 -> 시간 갱신

import sys
input = sys.stdin.readline

N = int(input())

meeting = []
for _ in range(N):
    s, e = map(int, input().split())
    meeting.append([s, e])

meeting.sort(key=lambda x:(x[1], x[0]))  # 종료 시간 순 정렬
c_end = meeting[0][1]
cnt = 1

for i in range(1, N):
    if meeting[i][0] >= c_end:
        cnt += 1
        c_end = meeting[i][1]

print(cnt)




# 와 이 반례는 생각도 못 했음
# 4 4
# 3 4
# 2 4
# x[1]로만 정렬하면 이 상태인데 여기선 4 4 후에 끝남
# 시작 시간도 포함해서 정렬하면 2 4, 4 4 가능 ..

# 틀렸습니다 ㅠ 근데 왜 틀린지 모르겠음
# import sys
# input = sys.stdin.readline
#
# N = int(input())
#
# meeting = [[0, 0]]
# for _ in range(N):
#     s, e = map(int, input().split())
#     meeting.append([s, e])
#
# meeting.sort(key=lambda x:x[1])
#
# c_end = meeting[0][1]
# cnt = 0
#
# for i in range(1, N+1):
#     if meeting[i][0] >= c_end:
#         cnt += 1
#         c_end = meeting[i][1]
#
# print(cnt)