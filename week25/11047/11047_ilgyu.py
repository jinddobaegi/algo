import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
# print(coins)

cnt = 0
for coin in coins:
    cnt += k // coin
    k %= coin
    # print(cnt, k)
print(cnt)