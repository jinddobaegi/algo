import sys
sys.stdin = open('input.txt')

def sol(n, a, b, c): # a 출발 b 보조 c 목표
    if n == 1:
        print(a, c)
    else:
        sol(n-1, a, c, b)
        sol(1, a, b, c)
        sol(n-1, b, a, c)


n = int(input())
print(2**n - 1)
if n <= 20:
    sol(n, 1, 2, 3)

