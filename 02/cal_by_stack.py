# 중위 표기 -> 후위 표기
# 중위표기식에서 토큰(하나씩) 읽음
# 피연산자면 출력
# 토큰이 연산자, 괄호면
# 스택의 top에 있는 연산자보다 우선순위 높으면 스택에 push
# 그렇지 않으면 스택 top의 연산자 우선순위가 낮아질 때까지 pop하고 토큰의 연산자를 push
# 토큰이 ')'이면 스택 top에 '('가 나올 때까지 스택에 pop하고 출력
# 토큰이 '('이면 pop만 하고 출력 x
# 중위표기식 다 읽었으면 스택에 남은 연산자를 모두 pop

fx = '(6+5*(2-8)/2)'

# 실제 우선순위
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}

# 스택 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}


res = ''
stack = [0] * len(fx)
top = -1

for x in fx:
    if x not in '(*/+-)':
        res += x
    elif x == ')':
        while stack[top] != '(':
            res += stack[top]
            top -= 1
        top -= 1
    else:
        # x와 top의 연산자 비교
        # 1) push 하는 경우 <- x 우선순위가 top보다 높거나, stack이 빈 경우
        if top == -1 or icp[x] > isp[stack[top]]:  # 조건 두 개 순서 바뀌면 안됨
            top += 1
            stack[top] = x
        # 2) top이 높거나 같은 경우
        else:
            # top이 낮아질 때까지, 혹은 stack이 빌 때까지 stack에서 꺼내서 res에 더해줌, 그 이후 stack에 push
            while icp[x] <= isp[stack[top]] and top > -1:
                res += stack[top]
                top -= 1
            top += 1
            stack[top] = x

print(res)


# 후위표기식 계산

stack = [0] * len(res)
top = -1

for x in res:
    if x not in '*/+-':
        top += 1
        stack[top] = x
    else:
        b = int(stack[top])
        top -= 1
        a = int(stack[top])
        if x == '+':
            stack[top] = a+b
        elif x =='-':
            stack[top] = a-b
        elif x == '*':
            stack[top] = a*b
        else:
            stack[top] = a//b

print(stack[top])