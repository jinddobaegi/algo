N, K = map(int, input().split())
coin = []

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse = True)
coin_cnt = 0

for i in coin:
    if K == 0:
        break
    coin_cnt += (K // i)
    K = K % i

print(coin_cnt)