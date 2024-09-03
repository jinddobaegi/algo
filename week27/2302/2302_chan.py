import sys
sys.stdin = open("week27/2302/2302.txt")
input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    
    vip = [0] * (M + 2)
    # print(vip)
    for i in range(1, M + 1):
        vip[i] = int(input())
    vip[M + 1] = N + 1
    # print(vip)
    
    dp = [0] * (N + 1) 
    dp[0] = 1
    dp[1] = 1
    # print(dp)
    if N > 1:
        dp[2] = 2
    
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    result = 1
    for i in range(1, M + 2):
        length = vip[i] - vip[i - 1] - 1
        result *= dp[length]
    
    print(result)

solution()