import sys
sys.stdin = open('input.txt')


s = int(input())
cnt = 0
if s == 1:
    print(1)
elif s == 2:
    print(1)
elif s == 3:
    print(2)
else:
    for i in range(1, s):
        s -= i
        if s >= 0:
            cnt += 1
        else:
            print(cnt)
            break
# 11047 동전 문제랑 접근 방식이 똑같음
