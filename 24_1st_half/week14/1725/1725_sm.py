# 히스토그램
# 플래5

# 로직
'''
!!그림 그려서 이해하기!!
가능한 높이를 다 구하고
나보다 낮은 애가 나오면, 낮은 높이에 나로부터의 가로거리 곱한 넓이값을 비교하면서 최댓값 구하기
근데 나보다 더 낮은 곳이 나오면? 재탐색해
'''

import sys
input = sys.stdin.readline

n = int(input())
graph = []
res = 0
left = 0

for _ in range(n):
    graph.append(int(input()))


#스택이 비워질 때까지 반복문이 슛됨
graph.append(0)


# 스택 초기화하기 (인덱스랑 높이 값을 튜플*** 로 저장할거임)
# 튜플 형태로 저장한거 잊지마...************************************
stack = [(0, graph[0])]

for now in range(1, n+1):
    left = now  # 현재 막대의 인덱스 값

    # 스택에서 젤 위에 있는 막대 높이가 현재 막대 높이( graph[now] )보다 크면
    while stack and stack[-1][1] > graph[now]:  # stack[-1[1] 최상단 높이
        # 현재 막대 인덱스 값, 스택에서 꺼낸 막대 높이 - 튜플 형태니까
        left, stack_height = stack.pop()  # 스택에서 그 높이 꺼내고


        # 여기부터 본격적으로 최대 넓이 구하기
        # 헷갈리면 적으면서 하자
        # now-left : 현재 값이랑 스택에서 꺼낸거 인덱스 사이 값
        res = max(res, stack_height * (now-left))


    # 처음에 이거 안 적어서 틀림
    # 돌거 다 돌고 처리한 다음에 현재 막대를 스택에 추가해줌 (체크만 해주는거)
    # 넓이 구할 때 안 쓰는 건데
    stack.append((left, graph[now]))

print(res)