N, K = map(int, input().split())
arr = list(map(int, input().split()))
lst = []

for i in range(1, N):
    lst.append(arr[i] - arr[i-1])  # 인접한 원생들끼리의 키 차이

lst.sort()
print(sum(lst[:N-K]))