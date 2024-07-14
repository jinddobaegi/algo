S = int(input())
sum = 0
cnt = 0
i = 1

while True:
    sum += i
    i += 1
    if sum > S:
        break
    cnt += 1

print(cnt)