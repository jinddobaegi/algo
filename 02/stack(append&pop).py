# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYmbJ8iqDdIDFARi&contestProbId=AYnVhb86_nYDFAUe&probBoxId=AYnVikgK_p4DFAUe&type=USER&problemBoxTitle=09-01+%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4+4&problemBoxCnt=5

T = int(input())

for tc in range(1, T+1):
    bracket = input()
    stack = []

    res = 1

    for b in bracket:
        if b =='(':
            stack.append(b)
        elif b ==')':
            if not stack:
                res = -1
                break
            else:
                stack.pop()
    if stack:
        res = -1

    print(f'#{tc} {res}')