from sys import stdin

input = stdin.readline

N = int(input())  # 대학의 수
lectures = []
for _ in range(N):
    p, d = map(int, input().split())
    # 금액을 음수로 넣어서 sort하면
    # 절댓값이 제일 큰 수가 맨 앞으로 오게 하기 위해서
    lectures.append((d, -p))

lectures.sort()  # 기한 빠른 순, 액수 큰 순

# d가 겹치는 강연들은
# 그 기한 안에 몇 개를 할 수 있는지가 관건
# 마지막 날짜를 갱신하는 주기를 언제로 해줘야 할까?
# 강연 기한 확인
# -> 마지막 강연 날짜보다 작거나 같으면 못함(어차피 금액순으로 정렬돼있어서 날짜가 같으면 앞에꺼가 큰 거임)
# 마지막 강연 날짜보다 크면 마지막 강연날짜+1 후 강연 함

total = 0
last_d = 0
for d, p in lectures:
    p = -p
    if d > last_d:
        total += p
        last_d += 1

print(total)