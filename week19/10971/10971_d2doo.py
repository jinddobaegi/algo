# 외판원 순회2
# 왜 combinations는 안되는거지?
import sys
from itertools import permutations

def move(lst):
    answer = 0

    for i in range(N - 1):
        if cost[lst[i]][lst[i + 1]] != 0:
            answer += cost[lst[i]][lst[i + 1]]
        else:  # 0이라면? 갈 수 없는 경우
            return 0

    if cost[lst[-1]][lst[0]] == 0:  # 되돌아 갈 수 없는 경우
        return 0
    else:
        answer += cost[lst[-1]][lst[0]]

    return answer


N = int(input()) # 도시의 수
cost = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(N)]
ans = sys.maxsize

for lst in permutations(num):
    res = move(lst)
    if res != 0:
        if ans > res:
            ans = res
print(ans)