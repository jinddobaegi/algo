import sys
sys.stdin = open('input.txt')

n = int(input())
seq = list(map(int, input().split()))
print(seq)

# dp로 하면 시간복잡도가 o(n^2)
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)
print(max(dp))







