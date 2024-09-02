import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
vip = []
for _ in range(m):
    v = int(input())
    vip.append(v)

seat = [i for i in range(1, n+1)]

fib = [0] * 41
fib[1] = 1
fib[2] = 2
fib[3] = 3
for i in range(4, 41):
    fib[i] = fib[i-1] + fib[i-2]
# print(fib)

# 일단 숫자는 피보나치 수 형태임
# 좌석 수  1  2  3  4
# 경우의수 1  2  3  5

# 좌석리스트를 vip기준으로 잘라서 경우의수 구한다음 다 곱해
if n == m:
    print(1)
else:
    ans = []
    cnt = 0 # vip좌석 전까지 몇개의 좌석이 있는지 카운팅
    for i in range(n):
        if seat[i] not in vip:
            cnt += 1
        else:
            # print(cnt)
            ans.append(fib[cnt])
            cnt = 0
        # 마지막 수 처리
        if i == n-1 and seat[i] not in vip:
            ans.append(fib[cnt])
    x = 1
    for num in ans:
        if num != 0:
            x *= num
    print(x)