# 게으른 백곰
# 투 포인터?

# 양동이 개수 N, 앨버트가 닿을 수 있는 거리 K
N, K = map(int, input().split())

# 배열을 저장하고 sort
bucket = []
for _ in range(N):
    ice, num = map(int, input().split())
    bucket.append((num, ice)) # 순서 헷갈려서 (양동이 좌표, 얼음 양) 으로 입력

bucket.sort() # 양동이 위치로 정렬
# print(bucket) # [(1, 5), (2, 2), (7, 4), (15, 10)]

# 거리 범위 내에 있으면 다 더해도 됨 ㅠㅠ
sum_ice, max_ice = 0, 0
start, end = 0, 0
while start <= end and end < N:
    if bucket[end][0] - bucket[start][0] <= 2 * K: # 좌우로 K니까 2K
        sum_ice += bucket[end][1]
        # print(f'end={end}')
        # print(f'sum_ice={sum_ice}')
        max_ice = max(sum_ice, max_ice)
        end += 1
    else:
        sum_ice -= bucket[start][1]
        start += 1
        # 뺀게 최대합일리 없으니까 여기선 max계산 안함

print(max_ice)