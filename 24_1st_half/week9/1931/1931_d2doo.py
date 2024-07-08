# 회의실 배정
# 1. 최대한 짧은것들중에 ({끝나는시간 - 시작하는시간} 정렬하기)
# 2. 겹치지 않는 애들 (끝나는 시간 정렬하면 됨)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(f'arr = {arr}')
# 1. 회의가 먼저 끝나는 애들 중 시작시간이 더 빠른애들 우선으로 정렬
arr.sort(key=lambda x : (x[1], x[0]))
# print(f'sort = {arr}')

ans = 1
end = arr[0][-1]
for i in range(1, n):
    if end <= arr[i][0]: # 회의 끝나자마자 시작해도 되니까 작거나 같아야함.
        ans += 1
        end = arr[i][1]

print(ans)

# pypy -> 127316kb | 408ms
# python3 -> 59068kb | 4096ms