# 하노이 탑 이동순서
# 이게 그건가 피보나치 그건가?
# f(n) = 2**n - 1

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, 6-start-end)
    print(start, end)
    hanoi(n - 1, 6-start-end, end)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 3)