# 시간 초과 코드 ㅠㅠ

# N, M = map(int, input().split())
# lst = [i for i in range(N)]
# answer = []
# cnt = 0
#
# while True: # 원처럼 삥글뺑글 돌려버리기
#     if len(lst) == 1: # 리스트 요소가 한개 남으면 멈춰
#         break
#
#     for i in range(len(lst)):
#         cnt += 1
#
#         if cnt == M:
#             a = lst.pop(0)
#             answer.append(a + 1)
#             cnt = 0
#             break
#         else:
#             elem = lst.pop(0) # 첫 요소를 빼고
#             lst.append(elem) # 뒤로 붙여
#
# answer.append(int(*lst) + 1)
# res = ', '.join(map(str, answer))
# print(f'<{res}>')

from collections import deque
N, M = map(int, input().split())
lst = deque(range(1, N + 1))
answer = []

while lst: # 원처럼 삥글뺑글 돌려버리기
    for _ in range(M-1): # M번째 보다 하나 전까지 요소 돌리고
        lst.append(lst.popleft()) # 첫 요소를 빼고 뒤로 붙여
    answer.append(lst.popleft()) # M번째 요소는 answer에 넣어

# res = ', '.join(map(str, answer))
print(str(answer).replace('[', '<').replace(']', '>'))
