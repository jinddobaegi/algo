# 균형잡힌 세상 
# 실버 4

import sys
sentence = ''

# .이 아닌게 나올 때까지 계속 입력 받을 것임
while sentence != '.':
    sentence = input()
    # 무한 입력 받다가 . 나오면 그때 break
    if sentence == '.':
        break

    # 스택에 검사할 괄호들을 담을 거야
    stack = []
    answer = 'yes'
    for check in sentence:
        # 일단 반복문 돌면서 여는 괄호는 다 담아
        if check == '(' or check == '[':
            stack.append(check)
        # 근데 닫는 괄호일 경우
        elif check == ')' or check == ']':
            # 스택의 길이가 0이면 닫는 괄호만 있는거니까 당연히 no인거지
            if len(stack) == 0:
                answer = 'no'
                break
            else:
                # 닫는 괄호일 경우
                if check == ']':
                    # 스택에 담긴 마지막 값이 그 짝에 맞는 여는 괄호면 스택에서 pop 해버림(짝이 맞는걸 확인했으니까!)
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        answer = 'no'
                        break
                elif check == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        answer = 'no'
                        break
                else:
                    answer = 'no'
                    break
    if len(stack) != 0:
        answer = 'no'
    print(answer)
