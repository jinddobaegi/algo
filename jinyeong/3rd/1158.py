# 요세푸스 문제
# N과 K가 주어짐
# 1 ~ N번 사람이 원 그리고 앉음
# K번째 사람 제거
# 그 다음 K번째 사람 제거
# N명이 모두 제거될 때까지
# 이때 제거되는 순서를 요세푸스 순열이라고 함

N, K = map(int, input().split())
people = [p + 1 for p in range(N)]

# 원형 큐 이용?
que = [0] * (K + 1)
front = 1
rear = 1


