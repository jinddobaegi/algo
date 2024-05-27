import sys
sys.stdin = open("week14/1725/1725.txt")
input = sys.stdin.readline

row = int(input())
graph = []
# 입력된 히스토그램의 높이를 리스트에 저장
for _ in range(row):
    graph.append(int(input()))
# 추가적인 0을 삽입하여 스택에 남아 있는 높이들을 처리할 수 있게 함
graph.append(0)

stack = []  # 스택을 이용하여 히스토그램의 인덱스를 저장
result = 0  # 최대 직사각형의 넓이를 저장하는 변수

# 전체 행(row) 수 + 1 만큼 반복
for i in range(row + 1):
    # 현재 막대의 높이가 스택에 저장된 인덱스의 막대 높이보다 작은 동안 반복
    while stack and graph[stack[-1]] > graph[i]:
        # 스택에서 인덱스를 꺼내고 그 인덱스에 해당하는 높이를 height에 저장
        height = graph[stack.pop()]
        # 현재 인덱스를 width로 설정
        width = i
        # 스택에 남아 있는 인덱스가 있다면 너비를 조정
        if stack:
            width -= stack[-1] + 1
        # 최대 직사각형 넓이를 갱신
        result = max(result, height * width)
    # 현재 인덱스를 스택에 추가
    stack.append(i)
    print("stack", stack)

# 최종 결과 출력
print(result)