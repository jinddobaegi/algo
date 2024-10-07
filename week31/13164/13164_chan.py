import sys
sys.stdin = open("week31/13164/13164.txt")

N, K = map(int, input().split())
height = list(map(int, input().split()))

# K개의 조로 나눈다 
# 각 조에는 한명이상 있어야함
# 조를 나눌때는 인접해야한다. (이걸머라고 하더라)
# 각조는 티셔트를 만든다. / 비용 = 키큰 - 키작은 / 혼자일경우 혼자서겠지
# 각조의 티셔츠 생산 최소비용의 합
# 근데 어케 3이나오지 10 - 6은 4아닌가..?
# 1 3 , 5 6, 10

# 인접한 원생 간의 키 차이를 계산
differences = []
for i in range(1, N):
    differences.append(height[i] - height[i - 1])

# 차이를 내림차순으로 정렬하고, K-1개의 큰 차이를 제거
differences.sort(reverse=True)

# 가장 큰 차이 K-1개를 제거하고 나머지 차이의 합을 구함
result = sum(differences[K-1:])

print(result)