# 수들의 합

S = int(input())
N = 0

while S >= 0:
    N += 1
    S -= N
    # print(f'S = {S} N = {N}')

print(N - 1) # 직전 while 문에서 꺼낸 N이어야하니까