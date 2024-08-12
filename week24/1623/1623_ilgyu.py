import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)

n = int(input())
score = [0] + list(map(int, input().split()))
parents = [0, 0] + list(map(int, input().split()))

tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    tree[parents[i]].append(i)

# dp[num][0]: num이 참석한 경우 최대 분위기 점수
# dp[num][1]: num이 참석하지 않은 경우 최대 분위기 점수
dp = [[0, 0] for _ in range(n + 1)]


def sol(num):
    dp[num][0] = score[num]  # num이 참석한 경우 초기화

    for child in tree[num]:
        sol(child) # 이게 제일 머리에 안들어옴

        # num이 참석한 경우 자식들이 참석 안한 dp의 최대값을 더해줌
        dp[num][0] += dp[child][1]

        # num이 참석하지 않은 경우 자식들이 참석하거나 참석하지 않은 경우의 최대값을 더해줌
        dp[num][1] += max(dp[child][0], dp[child][1])

sol(1)

# 참석자 명단 역추적
included = []


def trace(num, include):
    if include == True:
        included.append(num)
        for child in tree[num]:
            trace(child, False)  # 참석했으므로 자식은 불참
    elif include == False:
        for child in tree[num]:
            if dp[child][0] > dp[child][1]:
                trace(child, True)
            else:
                trace(child, False)


# 1번 노드가 참석한 경우
trace(1, True)
included.sort()
included.append(-1)
print(dp[1][0], dp[1][1])
print(" ".join(map(str, included)))

# 초기화 후 1번 노드가 참석하지 않은 경우
included = []
trace(1, False)
included.sort()
included.append(-1)
print(" ".join(map(str, included)))



## 메모리 초과 코드
# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# n = int(input())
# score = [0] + list(map(int, input().split()))
# parents = [0, 0] + list(map(int, input().split()))
#
# tree = [[] for _ in range(n + 1)]
# for i in range(2, n + 1):
#     tree[parents[i]].append(i)
#
# dp = [[[0, []], [0, []]] for _ in range(n + 1)]
#
# # dp[1][0] => 1이 참석한 경우의 분위기값, 참석자 명단
# # dp[1][1] => 1이 참석 안한 경우 분위기값, 참석자 명단
#
# def sol(num):
#     # num이 참석한 경우 => 자식 요소들은 강제로 못 넣음
#     dp[num][0][0] += score[num]
#     dp[num][0][1].append(num)
#
#     for child in tree[num]:
#         sol(child)
#         # num이 참석하면 그 자식이 참석안한 최대값을 추가해줌
#         dp[num][0][0] += dp[child][1][0]
#         dp[num][0][1] += dp[child][1][1]
#
#         # num이 참석을 안하면
#         if dp[child][0][0] > dp[child][1][0]:
#             dp[num][1][0] += dp[child][0][0]
#             dp[num][1][1] += dp[child][0][1]
#         else:
#             dp[num][1][0] += dp[child][1][0]
#             dp[num][1][1] += dp[child][1][1]
#
# sol(1)
#
# print(dp[1][0][0], dp[1][1][0])
# dp[1][0][1].sort()
# dp[1][0][1].append(-1)
# dp[1][1][1].sort()
# dp[1][1][1].append(-1)
# print(" ".join(map(str, dp[1][0][1])))
# print(" ".join(map(str, dp[1][1][1])))