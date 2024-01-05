T = int(input())


def preorder(n):
    global count
    if n:
        count += 1
        preorder(ch1[n])
        preorder(ch2[n])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E+1
    arr = list(map(int, input().split()))

    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)

    for i in range(E):
        if ch1[arr[i*2]] == 0:
            ch1[arr[i*2]] = arr[i*2+1]
        else:
            ch2[arr[i*2]] = arr[i*2+1]

    count = 0

    preorder(N)

    print(f'#{tc} {count}')