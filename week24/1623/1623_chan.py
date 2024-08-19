# 첫째 줄에 사장을 포함한 모든 직원의 수 N이 주어진다.
# (2≤N≤200,000) 사장은 1번이며,
# 다른 직원들은 2번부터 N번까지 차례로 번호가 매겨져 있다. 
# 둘째 줄에는 사장을 포함한 모든 직원의 "날라리 기질"을 나타내는 N개의 정수가 빈 칸을 사이에 두고 
# 1번 직원(사장)부터 N번 직원까지 순서대로 주어진다. 주어지는 정수는 절댓값이 10,000을 넘지 않는다. 
# 셋째 줄에는 사장을 제외한 모든 직원의 직속 상관의 번호를 나타내는 N-1개의 정수가 빈 칸을 사이에 두고 
# 2번 직원부터 N번 직원까지 순서대로 주어진다. 주어지는 수는 물론 N 이하의 자연수이며, 
# 항상 루트가 있는 트리 형태의 구조를 갖도록 입력이 주어진다고 가정해도 좋다.

import sys
sys.stdin = open("week24/1623/1623.txt")
input = sys.stdin.readline
import heapq

def test(node):
    dp[node][1] = weights[node] # -10 5 15 -5 20 10
    print(dp[node][1])
    for child in tree[node]:
        print("child", child, "node", node)
        test(child)
        dp[node][0] += max(dp[child][0], dp[child][1])
        dp[node][1] += dp[child][0]
    

N = int(input())
weights = [0] + list(map(int, input().split())) # 사장부터 ~ N번까지 날라리 기질
parents = list(map(int, input().split())) # 2번부터 ~ N번까지의 부모
dp = [[0, 0] for _ in range(N + 1)]
tree = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    tree[parents[i-2]].append(i)
print("weight", weights)
print("tree", tree)

test(1)
print(dp)

# for i in tree:
#     print(i)
