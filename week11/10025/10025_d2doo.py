# 게으른 백곰

# 양동이 개수 N, 앨버트가 닿을 수 있는 거리 K
N, K = map(int, input().split())

# 배열을 저장하고 sort
bucket = []
for _ in range(N):
    ice, num = map(int, input().split())
    bucket.append((ice, num))

bucket.sort(key=lambda x : x[1]) # 정렬했으니 - K 번째 양동이는 안 더해도됨
print(bucket)

# 거리 범위 내에 있으면 다 더해도 됨 ㅠㅠ