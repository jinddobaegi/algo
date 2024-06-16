# 트리의 독립 집합
# 골드1

'''
ㅎㅏ.. 트리..
'''

import sys
input = sys.stdin.readline


# 이거 답은 나오는데 메모리 초과..

n = int(input())
dp = [0 for _ in range(n+1)]
bt = list(range(n+1))


bt_result = []
w = list(map(int, input().split()))
ad = [[0 for _ in range(n+1)] for _ in range(n+1)] # 인접한 노드 연결 정도

for i in range(n-1):
    start, end = map(int, input().split())
    ad[start][end] = 1
    ad[end][start] = 1


def backTrack(i):
    bt_result.append(i)
    if (i == bt[i]):
        return
    backTrack(bt[i])

for i in range (1, n+1):
    max_v = w[i-1]
    bt[i] = i

    for j in range(1, i):
        if (ad[i][j] == 0 & max_v < dp[j] + w[i-1]):
            max_v = dp[j] + w[i-1]
            bt[i] = j
    dp[i] = max_v

print(dp[-1])
backTrack(n)
bt_result.reverse()
print(*bt_result)