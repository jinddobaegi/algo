import sys
input = sys.stdin.readline

N = int(input())  # 가로 칸의 수
stack = []
h_lst = []
max_s = 0

for _ in range(N):
    h = int(input())  # 높이
    h_lst.append(h)

for i in range(N):
    idx = i
    while stack and stack[-1][1] > h_lst[i]:   # 스택에 값이 존재하면 큰 값 만날 때까지 pop
        idx, h = stack.pop()
        # (현재 인덱스 - 해당 인덱스) 차이와 꺼낸 높이를 곱해 직사각형 넓이 계산 후 갱신
        max_s = max(max_s, (i-idx) * h)
    stack.append([idx, h_lst[i]])

while stack:
    idx, h = stack.pop()
    max_s = max(max_s, (N-idx) * h)

print(max_s)