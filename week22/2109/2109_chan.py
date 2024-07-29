import sys
sys.stdin = open("week22/2109/2109.txt")
input = sys.stdin.readline

# N = int(input())

# graph = [0] * (10000+1)

# for _ in range(N):
#     pay, day = map(int, input().split())
#     if graph[day] < pay:
#         graph[day] = pay

# result = 0
# for i in range(10001):
#     if graph[i] != 0:
#         result += graph[i]    
#     continue
# print(result)

import heapq

def max_earnings(n, lectures):
    # 일자 기준으로 정렬 (d 오름차순)
    lectures.sort(key=lambda x: x[1])
    
    max_heap = []
    total_earnings = 0
    
    for pay, day in lectures:
        # 현재 강연을 max_heap에 추가
        heapq.heappush(max_heap, pay)
        print('max_heap = ', max_heap)
        
        # 만약 max_heap의 길이가 day보다 크다면 가장 작은 값을 제거
        if len(max_heap) > day:
            heapq.heappop(max_heap)
    
    # max_heap에 남아있는 값들의 합을 구해서 최종 수익 계산
    total_earnings = sum(max_heap)
    
    return total_earnings

# 입력
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
print(lectures)

# 최대 수익 계산
result = max_earnings(n, lectures)
print(result)