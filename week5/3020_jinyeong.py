from sys import stdin
input = stdin.readline

N, H = map(int, input().split())
# N: 가로 길이 [2, 20만]
# H: 세로 길이 [2, 50만]

# N개의 석순,종유석을 순서대로 받음
# 길이는 무조건 H보다 작음

# 배열 만들어서 직접 하면 시간초과 뜰 것 같다는 생각이 강하게 듦

# 뭔가 숫자 그 자체를 이용해서
# 높이 차를 구해서 어떻게 저떻게 하는 방법을 써야 하지 않을까...?

# 종유석: "높이 - 종유석길이" 하면 빈 구간을 알 수 있음
# x번째 구간 => 밑에서 1부터 세서 x번째임
# 순서가 중요한 게 아님
# 석순이랑 종유석 리스트를 따로 만들어서 몇 이상, 몇 이하인 걸 개수를 알아볼까..?

arr = list(list() for _ in range(2))
# arr[0]: 석순 길이 리스트
# arr[1]: 종유석이 "없는" 길이 리스트

for i in range(N):
    length = int(input()) if (i%2==0) else (H-int(input()))  # 종유석이면 종유석이 없는 길이
    arr[i%2].append(length)

# 지나갈 구간 높이가
# arr[0]의 원소 값보다 작거나 같고
# arr[1]의 원소 값보다 크면 부딪힘
totals = []
for h in range(1, H+1):
    # 구간 높이가 h일 때
    a = len(list(filter(lambda x: x >= h, arr[0])))  # 부딪히는 석순 수
    b = len(list(filter(lambda y: y < h, arr[1])))   # 부딪히는 종유석 수
    total = a + b  # 파괴하는 수
    totals.append(total)

min_v = min(totals)
cnt = totals.count(min_v)
# print(totals)

print(min_v, cnt)

# pypy로 돌렸을 때 4%에서 시간초과 ㅋㅋ