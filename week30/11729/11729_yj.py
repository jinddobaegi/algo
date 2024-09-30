N = int(input())

def hanoi(N, s, e):
    if N == 1:  # 원판이 하나인 경우
        print(s, e)
        return

    hanoi(N-1, s, 6-s-e)
    print(s, e)
    hanoi(N-1, 6-s-e, e)

print(2**N-1)
hanoi(N, 1, 3)