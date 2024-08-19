# 동전
# 그리디

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True) # 나눠서 정수의 몫이 떨어지는 가장 큰 수 부터 나눠야함

min_cnt = 0
for coin in coins:
    min_cnt += K // coin # 첫번째 예시라면 1000 * 4개 + 100 * 2개 
    K = K % coin

print(min_cnt)