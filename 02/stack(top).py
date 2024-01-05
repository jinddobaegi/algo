# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbJ8iqDdIDFARi&contestProbId=AYnVhb86_nYDFAUe&probBoxId=AYnVikgK_p4DFAUe&type=USER&problemBoxTitle=09-01+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4+4&problemBoxCnt=5

T = int(input())


def my_push(x):
    global top
    top += 1
    stack[top] = x
    return


def my_pop():
    global top
    if top == -1:
        return 'underflow'
    else:
        top -= 1
        return stack[top+1]


for tc in range(1, T+1):
    bracket = input()
    b_len = len(bracket) - 1
    stack = [0] * b_len
    top = -1
    res = 1
    for b in bracket:
        if b == '(':
            my_push(b)
        elif b == ')':
            temp = my_pop()
            if temp == 'underflow':
                res = -1
                break
    if top != -1:
        res = -1

    print(f'#{tc} {res}')