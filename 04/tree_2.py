from collections import deque


def postorder(x):
    if x:
        postorder(ch1[x])
        postorder(ch2[x])
        search_order.append(tree[x])


def my_cal(my_list):
    dq = deque()
    for x in my_list:
        if x not in '*/+-':
            dq.append(int(x))
        else:
            num2 = dq.pop()
            num1 = dq.pop()
            if x == '+':
                dq.append(num1 + num2)
            elif x == '-':
                dq.append(num1 - num2)
            elif x == '*':
                dq.append(num1 * num2)
            else:
                dq.append(num1 // num2)
    return dq[0]


for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for i in range(N):
        info = list(map(str, input().split()))
        if len(info) == 2:
            nn, nv = info
            nn = int(nn)
            tree[nn] = nv
        else:
            nn, op, c1, c2 = info
            nn = int(nn)
            c1 = int(c1)
            c2 = int(c2)
            tree[nn] = op
            ch1[nn] = c1
            ch2[nn] = c2

    search_order = []

    postorder(1)
    res = my_cal(search_order)

    print(f'#{tc} {res}')