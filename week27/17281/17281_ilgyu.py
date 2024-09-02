import sys
sys.stdin = open('input.txt')
from itertools import permutations

n = int(input())
s = []
for _ in range(n):
    x = list(map(int, input().split()))
    s.append(x)

# 4번타자 고정
# 0이 3번 나오면 종료, 아니면 이닝 이어감
# 4 0 0 0 0 0 0 0 0
# 1번선수는 홈런치는 선수, 2번선수는 아웃

# 2
# 4 0 0 0 1 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 경우의 수
# 0 0 0 4 1 1 1 0 0
# 0 0 0 4 0 1 1 1 0 ...

# s에서 리스트 하나하나 꺼내가지고 경우의수를 따지기
ans = 0
for t in permutations((range(1, 9)), 8):
    t = list(t[:3]) + [0] + list(t[3:]) # 1번선수가 4번타자 고정
    # t는 타자 출전 순서의 경우의 수
    # print(t)
    # t에서 리스트의 값들 1, 2, 3.. 이거 자체는 그냥 선수구분용이지 별의미없음

    # 순열로 선수들의 출전순서를 만든 다음
    # for문으로 인풋값으로 받은 이닝들을 돌면서 점수 계산
    # 이러면 문제조건대로 처음정한 선수들의 순서는 계속 유지된상태로 이닝 진행

    hitter = 0 # 현재타자(인덱스 값)
    res = 0 # 이번이닝 점수
    for i in range(n):
        out = 0 # 현재 몇 아웃인지
        base = [0, 0, 0, 0] # 각 베이스에 몇명 있는지

        while out < 3:
            hit = s[i][t[hitter]] # 현재타자가 1~4중 뭐칠건지

            if hit == 0:
                out += 1
            elif hit == 1: # 안타
                res += base[3] # 3루에 주자있으면 안타일 때 그만큼 점수 먹으니까
                base = [0, 1, base[1], base[2]] # 한칸씩 값들이 전진

            elif hit == 2:
                res += base[2] + base[3] # 2칸 전진이니까 2루, 3루 수만큼 점수 +
                base = [0, 0, 1, base[1]]

            elif hit == 3:
                res += base[1] + base[2] + base[3]
                base = [0, 0, 0, 1]

            elif hit == 4:
                res += base[1] + base[2] + base[3] + 1
                base = [0, 0, 0, 0]

            hitter = (hitter + 1) % 9 # 다음타자 불러오기

    if res > ans:
        ans = res
print(ans)





