N = int(input())
stack = []  # 인덱스, 값
finish = 0 # 인덱스들의 차(가로) * 값(세로) : 넓이

for i in range(N):
    value = int(input())
    start = i # while 문에 안 들어갈 수도 있으니까
    while stack and stack[-1][1] >= value:
        start, pre_value = stack.pop() # 마지막으로 갱신한 값 저장
        finish = max(finish,(i-start)*pre_value)
    stack.append([start, value])

while stack : # 스택에 값이 남았을 수도 있으니까
    start, pre_value = stack.pop()
    finish = max(finish,(N-start)*pre_value)

print(finish)