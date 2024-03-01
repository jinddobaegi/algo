sentence = []
while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    answer = "yes"

    for i in sentence:
        # i의 경우를 3가지로 나눈다.
        if i == '.':  # 1. 마침표: 문장 끝.
            if stack:
                answer = "no"
            break

        elif i == '(' or i == '[':  # 2. 여는 괄호
            stack.append(i)

        elif i == ')' or i == ']':  # 3. 닫는 괄호
            if not stack:  # 스택이 비어있으면?
                answer = "no"
                break

            else:  # 스택에 뭔가 있긴 있는데
                if i == ')':  # i가 닫는 소괄호인 경우
                    if stack[-1] == '(':  # 스택의 top이 여는 소괄호일때는
                        stack.pop()  # 스택에서 빼내주고
                    else:
                        answer = "no"  # 그게 아니면 멈춰
                        break
                if i == ']':  # i가 닫는 대괄호인 경우
                    if stack[-1] == '[':  # 스택의 top이 여는 대괄호일때는
                        stack.pop()  # 스택에서 빼내주고
                    else:
                        answer = "no"  # 아니면 멈춰
                        break
    if stack:
        answer = "no"
    print(answer)
